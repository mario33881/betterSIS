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
    import bettersis.version_parser as version_parser
except ImportError:
    from _version import __version__  # noqa: F401
    import version_parser

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
ghreleases_apiurl = "https://api.github.com/repos/mario33881/bettersis/releases"


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

    versions_strings = []
    for data in releases_data:
        if "tag_name" in data.keys():
            versions_strings.append(data["tag_name"])
    
    versions = []
    for version_string in versions_strings:
        versions.append(version_parser.parse_version(version_string))

    versions.sort()

    old_versions = versions
    if len(versions) > 1:
        old_versions = versions[:-1]

    return old_versions


def check_updates(t_ghreleases_apiurl, t_curr_version):
    """
    Checks for updates.

    :param str t_ghreleases_apiurl: api url for gh releases
    :param str t_curr_version: current version
    :return dict res: dictionary with success status, errors, update_version, update_available
    """
    res = {"success": False, "errors": [], "latest_version": None, "update_available": False}

    try:
        with urllib.request.urlopen(
            t_ghreleases_apiurl + "/latest",
            context=ssl.create_default_context(cafile=certifi.where())
        ) as url:
            latest_release_data = json.loads(url.read().decode())

        if "tag_name" in latest_release_data.keys():
            latest_version_string = latest_release_data["tag_name"]

            current_version = version_parser.parse_version(t_curr_version)
            latest_version = version_parser.parse_version(latest_version_string)

            res["success"] = True
            res["latest_version"] = str(latest_version)

            if latest_version > current_version:
                # An update is available
                res["update_available"] = True
                logger.debug("[CHECK_UPDATES] Found an update: version {}".format(res["latest_version"]))
            else:
                logger.debug("[CHECK_UPDATES] No updates found")
        else:
            logger.error("[CHECK_UPDATES] Somehow, the latest version doesn't have a tag name", exc_info=True, stack_info=True)
            res["errors"].append("[CHECK_UPDATES] Somehow, the latest version doesn't have a tag name")
    except Exception as e:
        logger.error("[CHECK_UPDATES] Error during update check: ", exc_info=True, stack_info=True)
        res["errors"].append(e)

    return res


def ask_user_input(t_options, t_details):
    """
    Ask the user for an input.
    The input has to be contained inside the ``<t_options>`` list.

    :param list t_options: possible options that the user can choose between
    :param str t_details: question shown to the user
    :return str user_input: option selected by the user, in lowercase letters
    """
    user_input = ""
    lowercase_options = [option.lower() for option in t_options]
    while user_input not in lowercase_options:
        user_input = input(t_details + " [" + "/".join(t_options) + "]:")
        user_input = user_input.strip().lower()

        if user_input not in lowercase_options:
            print("Incorrect input. Please choose one between: " + ", ".join(t_options))
    
    return user_input


def delete_old_appimages():
    """
    If the user wants to, delete all the old AppImages of BetterSIS

    If an old AppImage is found, ask the user if they want to
    delete all the old AppImages using the ask_user_input() function.
    """
    found_first_old_version = False
    wants_delete = False

    for version in get_old_versions(ghreleases_apiurl):
        version_path = os.path.join(os.environ["APPDIR"], "BetterSIS-" + str(version) + "-x86_64.AppImage")
        if os.path.isfile(version_path) or os.path.isfile(version_path + ".zs-old"):
            if not found_first_old_version:
                # found the first old version:
                # ask the user if they want to delete all the old versions
                found_first_old_version = True
                user_input = ask_user_input(["y", "n"], "Found old AppImage(s): do you want to delete it(them)?")

                if user_input == "y":
                    wants_delete = True

        if wants_delete and os.path.isfile(version_path):
            os.remove(version_path)

        if wants_delete and os.path.isfile(version_path + ".zs-old"):
            os.remove(version_path + ".zs-old")


def update_appimage():
    """
    If this function was run in an appimage and there are updates,
    download the latest AppImage and ask the user if they want to
    delete old versions (if present).

    :return bool success: True if the check for updates was successful
    """
    success = False
    update_info = check_updates(ghreleases_apiurl, __version__.split(" ")[1])

    using_appimage = "APPIMAGE" in os.environ and "APPDIR" in os.environ
    try:
        if not using_appimage:
            print("Can't check for updates: it looks like you are not running the AppImage version")
            return success

        if update_info["success"]:
            if update_info["update_available"]:
                aiut_path = os.path.join(os.environ["APPDIR"], "appimageupdate", "AppRun")
                subprocess.call([aiut_path, os.environ["APPIMAGE"]])
                delete_old_appimages()
            else:
                print("Already using latest version. No new updates found.")

            success = True
        else:
            print("Couldn't get releases data")

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

    print("\nUser input:")
    u_in = ask_user_input(["Yes", "No", "Maybe"], "Does this work?")
    print("user entered:", u_in)
