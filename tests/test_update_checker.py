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
