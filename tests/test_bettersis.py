#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST_BETTERSIS: tests bettersis.py
"""

__author__ = "Zenaro Stefano"
__version__ = "2021-01-08 1.0.0"

import os
import sys
import unittest

# import bettersis from the ../bettersis folder
curr_dir = os.path.realpath(os.path.dirname(__file__))
bettersis_path = os.path.join(curr_dir, "..", "bettersis")
sys.path.insert(1, os.path.realpath(bettersis_path))
import bettersis


class TestBettersis(unittest.TestCase):
    """
    Tests bettersis.py
    """

    def test_production(self):
        """
        Makes sure that we are in production mode.
        """
        self.assertFalse(bettersis.boold, "boold should be False in production mode")


if __name__ == "__main__":
    unittest.main()
