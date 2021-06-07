#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**BETTERSIS.UPDATE_CHECKER**:
contains function that help BetterSIS to check for updates
"""

__author__ = "Zenaro Stefano"

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


def check_updates(t_ghreleases_apiurl, t_version):  # noqa: C901
    """
    Checks for updates.

    :param str t_version: current version
    :param str t_ghreleases_apiurl: api url for gh releases
    :return dict res: dictionary with success status, errors, update_version, update_available
    """
    res = {"success": False, "errors": [], "update_version": None, "update_available": False}

    try:
        current_version = extract_version(t_version)

        if current_version["success"]:
            # Get Github Releases information
            with urllib.request.urlopen(
                t_ghreleases_apiurl,
                context=ssl.create_default_context(cafile=certifi.where())
            ) as url:
                releases_data = json.loads(url.read().decode())

            latest_data = {"success": False, "major_version": 0, "minor_version": 0, "patch_version": 0}

            # get latest version from Github Releases
            for data in releases_data:
                if "tag_name" in data.keys():
                    tag_name = data["tag_name"]
                    version_data = extract_version(tag_name)

                    if version_data["success"]:
                        latest_data["success"] = True
                        if version_data["major_version"] > latest_data["major_version"]:
                            latest_data["major_version"] = version_data["major_version"]

                        if version_data["minor_version"] > latest_data["minor_version"]:
                            latest_data["minor_version"] = version_data["minor_version"]

                        if version_data["patch_version"] > latest_data["patch_version"]:
                            latest_data["patch_version"] = version_data["patch_version"]

            if latest_data["success"]:
                res["success"] = True
                dotted_last_version = "{}.{}.{}".format(latest_data["major_version"],
                                                        latest_data["minor_version"],
                                                        latest_data["patch_version"])

                # if one of the "ifs" is true, the currently running version is not the latest version
                if latest_data["major_version"] > current_version["major_version"]:
                    res["update_available"] = True
                    res["update_version"] = dotted_last_version

                elif latest_data["major_version"] == current_version["major_version"]:
                    if latest_data["minor_version"] > current_version["minor_version"]:
                        res["update_available"] = True
                        res["update_version"] = dotted_last_version

                    elif latest_data["minor_version"] == current_version["minor_version"]:
                        if latest_data["patch_version"] > current_version["patch_version"]:
                            res["update_available"] = True
                            res["update_version"] = dotted_last_version

    except Exception as e:
        logger.error("[UPDATES] Error during update check: ", exc_info=True, stack_info=True)
        res["errors"].append(e)
    else:
        logger.debug("[UPDATES] Checked updates: last version found"
                     " is version {}, update available? {}".format(dotted_last_version, res["update_available"]))
    return res


if __name__ == "__main__":

    import pprint
    ghreleases_apiurl = "https://api.github.com/repos/mario33881/bettersis/releases"

    print("This is a simple test for this module:")

    updates = check_updates(ghreleases_apiurl, "0.0.0")
    print("Update found: ")
    pprint.pprint(updates)

    noupdates = check_updates(ghreleases_apiurl, "999.999.999")
    print("\nNo Update found: ")
    pprint.pprint(noupdates)
