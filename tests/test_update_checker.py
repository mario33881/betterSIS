#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST_UPDATE_CHECKER: tests update_checker.py
"""

__author__ = "Zenaro Stefano"
__version__ = "2021-01-08 1.0.0"

import os
import sys
import unittest

# import update_checker.py from the ../bettersis folder
curr_dir = os.path.realpath(os.path.dirname(__file__))
bettersis_path = os.path.join(curr_dir, "..", "bettersis")
sys.path.insert(1, os.path.realpath(bettersis_path))
import update_checker
import _version


class TestUpdateChecker(unittest.TestCase):
    """
    Tests update_checker.py
    """

    def test_extract_version(self):
        """
        Tests extract_version() function: 
        extracts the version numbers from a string.
        """
        ver_data = update_checker.extract_version("")
        self.assertFalse(ver_data["success"], "empty string doesn't contain a correct version")
        self.assertIsNone(ver_data["major_version"])
        self.assertIsNone(ver_data["minor_version"])
        self.assertIsNone(ver_data["patch_version"])

        ver_data = update_checker.extract_version(".")
        self.assertFalse(ver_data["success"], "one dot is not a correct version")
        self.assertIsNone(ver_data["major_version"])
        self.assertIsNone(ver_data["minor_version"])
        self.assertIsNone(ver_data["patch_version"])

        ver_data = update_checker.extract_version("..")
        self.assertFalse(ver_data["success"], "the string '..' doesn't contain version numbers")
        self.assertIsNone(ver_data["major_version"])
        self.assertIsNone(ver_data["minor_version"])
        self.assertIsNone(ver_data["patch_version"])

        ver_data = update_checker.extract_version("a.b.c")
        self.assertFalse(ver_data["success"], "the string 'a.b.c' doesn't contain version numbers")
        self.assertIsNone(ver_data["major_version"])
        self.assertIsNone(ver_data["minor_version"])
        self.assertIsNone(ver_data["patch_version"])

        ver_data = update_checker.extract_version("1.c.0")
        self.assertFalse(ver_data["success"], "the string '1.c.0' doesn't contain version numbers")
        self.assertIsNone(ver_data["major_version"])
        self.assertIsNone(ver_data["minor_version"])
        self.assertIsNone(ver_data["patch_version"])

        ver_data = update_checker.extract_version("-1.4.3")
        self.assertFalse(ver_data["success"], "the string '-1.4.3' doesn't contain version "
                                              "numbers (negative numbers are not allowed)")
        self.assertIsNone(ver_data["major_version"])
        self.assertIsNone(ver_data["minor_version"])
        self.assertIsNone(ver_data["patch_version"])

        ver_data = update_checker.extract_version("1.2.3")
        self.assertTrue(ver_data["success"], "the string '1.2.3' is a correct version")
        self.assertEqual(ver_data["major_version"], 1)
        self.assertEqual(ver_data["minor_version"], 2)
        self.assertEqual(ver_data["patch_version"], 3)
    
    def test_check_updates(self):
        """
        Tests check_updates() function: tells if an update is available 
        and, if so, which version is the latest version.
        """
        cu_data = update_checker.check_updates("https://api.github.com/repos/mario33881/bettersis/releases",
                                               "0.0.0")
        self.assertTrue(cu_data["success"], "check was successfull")
        self.assertTrue(cu_data["update_available"], "a new version should be available")

        cu_data = update_checker.check_updates("https://api.github.com/repos/mario33881/bettersis/releases",
                                               "9999.9999.9999")

        self.assertTrue(cu_data["success"], "check was successfull")
        self.assertFalse(cu_data["update_available"], "a new version should not be not available")

        current_version = _version.__version__.split(" ")[1]
        cu_data = update_checker.check_updates("https://api.github.com/repos/mario33881/bettersis/releases",
                                               current_version)
        self.assertTrue(cu_data["success"], "check was successfull")
        self.assertFalse(cu_data["update_available"], "this should be the latest version")


if __name__ == "__main__":
    unittest.main()
