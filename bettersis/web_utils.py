#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**BETTERSIS.WEB_UTILS**:
web utilities used to manage web pages
"""

__author__ = "Zenaro Stefano"

import os
import webbrowser

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401


def open_browser(t_url, t_details=""):
    """
    Tries to open ``<t_url>`` page with a browser.

    If the user is root, browsers will fail to open:
    the function will print a message to the user to open the url manually

    ``<t_details>`` is shown before "page" inside messages.

    Example:

    .. code-block:: python

        >>> details = "tutorials"
        >>> tutorials_page = "http://www.example.com/index.html"
        >>> open_browser(tutorials_page, details)
        Trying to open the tutorials page on a browser... Done, the webpage is open
        # if running as root:
        Trying to open the tutorials page on a browser... can't open the browser because you are running betterSIS as root!
        You can find the tutorials page at this URL: http://www.example.com/index.html

    :param str t_url: url to open
    :param str t_details: details about the page
    :return bool success: True if the browser was opened successfully
    """
    success = False

    print("Trying to open the " + t_details + " page on a browser... ", end="")

    try:
        # try to "make a folder" a file to test if root (and then delete it)
        os.mkdir('/etc/random_not_existing_directory_name.very_specific')
        os.rmdir('/etc/random_not_existing_directory_name.very_specific')

        print("can't open the browser because you are running betterSIS as root!\n")
        print("You can find the " + t_details + " page at this URL: ", t_url)

    except PermissionError:
        webbrowser.open(t_url)
        print("Done, the webpage is open")
        success = True

    return success
