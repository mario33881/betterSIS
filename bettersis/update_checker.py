#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**BETTERSIS.UPDATE_CHECKER**:
contains function that help BetterSIS to check for updates
"""

__author__ = "Zenaro Stefano"

import os
import subprocess
import logging
import urllib.request
import json
import ssl

import certifi

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
ghreleases_apiurl = "https://api.github.com/repos/mario33881/bettersis/releases"


def extract_version(version_string):
    """
    Extract major, minor and path number from ``<version_string>``.

    :param str version_string: string with the version (ex. '1.0.0')
    :return dict res: result of the operation (success boolean and parsed data)
    """
    res = {
        "success": False,
        "major_version": None,
        "minor_version": None,
        "patch_version": None
        }

    v_version = version_string.split(".")
    if len(v_version) == 3:
        major_version = v_version[0]
        minor_version = v_version[1]
        patch_version = v_version[2]

        try:
            # string must contain integers
            major_version = int(major_version)
            minor_version = int(minor_version)
            patch_version = int(patch_version)

            # those integers must be positive
            if major_version >= 0 and minor_version >= 0 and patch_version >= 0:
                res["major_version"] = int(major_version)
                res["minor_version"] = int(minor_version)
                res["patch_version"] = int(patch_version)

                res["success"] = True

        except ValueError:
            pass

    return res


def get_old_versions(t_ghreleases_apiurl):
    """
    Returns a list of old versions.

    First the function collects all the releases in a list and then
    removes the latest release from the list.

    :param str t_ghreleases_apiurl: api url for gh releases
    :return list versions: old versions
    """
    with urllib.request.urlopen(
        t_ghreleases_apiurl,
        context=ssl.create_default_context(cafile=certifi.where())
    ) as url:
        releases_data = json.loads(url.read().decode())

    versions = []
    for data in releases_data:
        if "tag_name" in data.keys():
            versions.append(data["tag_name"])

    with urllib.request.urlopen(
        t_ghreleases_apiurl + "/latest",
        context=ssl.create_default_context(cafile=certifi.where())
    ) as url:
        latest_release_data = json.loads(url.read().decode())

    if "tag_name" in latest_release_data.keys():
        versions.remove(latest_release_data["tag_name"])

    return versions


def check_updates(t_ghreleases_apiurl, t_version):  # noqa: C901
    """
    Checks for updates.

    :param str t_version: current version
    :param str t_ghreleases_apiurl: api url for gh releases
    :return dict res: dictionary with success status, errors, update_version, update_available
    """
    res = {"success": False, "errors": [], "latest_version": None, "update_available": False}

    try:
        current_version = extract_version(t_version)

        if current_version["success"]:
            # Get Github Releases information
            with urllib.request.urlopen(
                t_ghreleases_apiurl + "/latest",
                context=ssl.create_default_context(cafile=certifi.where())
            ) as url:
                latest_release_data = json.loads(url.read().decode())

            if "tag_name" in latest_release_data.keys():
                tag_name = latest_release_data["tag_name"]
                logger.debug("Found latest release version: " + tag_name)
                res["latest_version"] = tag_name
                latest_version_data = extract_version(tag_name)

                if latest_version_data["success"]:
                    res["success"] = True

                    # if one of the "ifs" is true, the currently running version is not the latest version
                    if latest_version_data["major_version"] > current_version["major_version"]:
                        res["update_available"] = True

                    elif latest_version_data["major_version"] == current_version["major_version"]:
                        if latest_version_data["minor_version"] > current_version["minor_version"]:
                            res["update_available"] = True

                        elif latest_version_data["minor_version"] == current_version["minor_version"]:
                            if latest_version_data["patch_version"] > current_version["patch_version"]:
                                res["update_available"] = True
                else:
                    e = "[CHECK_UPDATES] Couldn't parse the latest version string '{}'".format(tag_name)
                    logger.error(e)
                    res["errors"].append(e)
        else:
            e = "[CHECK_UPDATES] Couldn't parse the current version string '{}'".format(t_version)
            logger.error(e)
            res["errors"].append(e)

    except Exception as e:
        logger.error("[CHECK_UPDATES] Error during update check: ", exc_info=True, stack_info=True)
        res["errors"].append(e)

    if res["update_available"]:
        logger.debug("[CHECK_UPDATES] Checked updates: latest version found"
                     " is version {}, update available? {}".format(res["latest_version"], res["update_available"]))
    return res


def update_appimage():  # noqa: C901
    """
    If this function was run in an appimage and there are updates,
    download the latest AppImage and ask the user if they want to
    delete old versions (if present).

    :return bool success: True if the check for updates was successful
    """
    success = False
    update_info = check_updates(ghreleases_apiurl, __version__.split(" ")[1])

    try:
        if "APPIMAGE" in os.environ and "APPDIR" in os.environ:
            if update_info["success"]:
                if update_info["update_available"]:
                    aiut_path = os.path.join(os.environ["APPDIR"], "appimageupdate", "AppRun")
                    subprocess.call([aiut_path, os.environ["APPIMAGE"]])
                else:
                    print("Already using latest version. No new updates found.")

                success = True

                found_old_version = False
                wants_delete = False

                for version in get_old_versions(ghreleases_apiurl):
                    version_path = os.path.join(os.environ["APPDIR"], "BetterSIS-" + version + "-x86_64.AppImage")
                    if os.path.isfile(version_path) or os.path.isfile(version_path + ".zs-old"):
                        if not found_old_version:
                            found_old_version = True
                            user_input = ""
                            while user_input not in ["y", "n"]:
                                user_input = input("Found an/many old AppImage(s): do you want to delete it? [y/n]: ")
                                user_input.strip().lower()

                            if user_input == "y":
                                wants_delete = True

                        if wants_delete and os.path.isfile(version_path):
                            os.remove(version_path)

                        if wants_delete and os.path.isfile(version_path + ".zs-old"):
                            os.remove(version_path + ".zs-old")
            else:
                print("Couldn't get releases data")
        else:
            print("Can't check for updates: it looks like you are not running the AppImage version")

    except Exception as e:
        print("Something went wrong during the update:", e)

    return success


if __name__ == "__main__":

    import pprint

    print("This is a simple test for this module:")

    updates = check_updates(ghreleases_apiurl, "0.0.0")
    print("Update found: ")
    pprint.pprint(updates)

    noupdates = check_updates(ghreleases_apiurl, "999.999.999")
    print("\nNo Update found: ")
    pprint.pprint(noupdates)

    print("\nOld versions:")
    pprint.pprint(get_old_versions(ghreleases_apiurl))
