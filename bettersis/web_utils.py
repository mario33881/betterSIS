#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**BETTERSIS.WEB_UTILS**:
Utilities used to manage web pages (or functions used by those utilities)
"""

__author__ = "Zenaro Stefano"

import random
import os
import string
import webbrowser

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401


def gen_rand_string(t_len):
    """
    Generates a random string of ``<t_len>`` length.

    The random string might be made of lowercase letters,
    uppercase letters, digits and/or a dot (".").

    :param int t_len: random string's length
    :return str rand_str: random string
    """
    ran_str = ''.join(random.choices(string.ascii_letters + string.digits + ".", k = t_len))
    return ran_str


def gen_non_existing_path(t_prefix=""):
    """
    Generates a path that is made of the ``<t_prefix>`` prefix
    and a random filename.

    The filename is made of at least 8 characters.

    If the path points to an existing file/folder, the function will
    increase the chances of finding a non existing path by using more than 8 random characters.

    Example:

    .. code-block:: python

        >>> gen_non_existing_path("/etc/")
        '/etc/S4vZS2vg'
        >>> gen_non_existing_path()
        '7VMOulqj'

    """
    filename_len = 8
    rand_filename = t_prefix + gen_rand_string(filename_len)
    while os.path.exists(rand_filename):
        filename_len += 2  # increase the chance of finding a non existing path
        rand_filename = t_prefix + gen_rand_string(filename_len)

    return rand_filename


def open_browser(t_url, t_details=""):
    """
    Tries to open ``<t_url>`` page with a browser.

    If the user is root, browsers will fail to open:
    the function will print a message to the user to invite them to open the url manually

    Since there is no universal way of knowing if a user has root privileges,
    this function tries to create a new folder inside the /etc/ folder:
    * if this succedes, the user is root and the folder gets deleted
    * if this fails, the user is not root
    * if somehow this function tries to create an existing folder, os.mkdir will throw an exception
    so there should be NO risks of deleting an existing folder

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

    rand_filename = gen_non_existing_path(t_prefix="/etc/")

    try:
        # try to make a folder to test if root (and then delete it)
        os.mkdir(rand_filename)
        os.rmdir(rand_filename)

        print("Can't open the browser because you are running betterSIS as root!\n")
        print("You can find the " + t_details + " page at this URL: ", t_url)

    except PermissionError:
        # not root, the default web browser will allow
        # this instruction to open the web page
        webbrowser.open(t_url)
        print("Done, the webpage is open")
        success = True

    except FileExistsError:
        # mkdir could try to make a folder that already exists.
        # this SHOULD NOT happen (because of the gen_non_existing_path() function)
        # but, in case this happens, success is going to be False
        print("Couldn't open the browser automatically!\n")
        print("You can find the " + t_details + " page at this URL: ", t_url)

    return success


if __name__ == "__main__":
    rnd_string = gen_rand_string(5)
    print("Generating random string of length 5: '{}' (len: {})".format(rnd_string, len(rnd_string)))

    rnd_string = gen_rand_string(15)
    print("Generating random string of length 15: '{}' (len: {})".format(rnd_string, len(rnd_string)))

    rnd_path = gen_non_existing_path()
    print("Generating random path in this folder:", rnd_path)

    print("Opening github.com on the default web browser")
    open_browser("https://github.com", "github.com")
