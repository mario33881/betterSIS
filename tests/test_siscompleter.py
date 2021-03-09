#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST_SISCOMPLETER: tests siscompleter.py
"""

__author__ = "Zenaro Stefano"
__version__ = "2021-01-06 1.0.0"

import os
import sys
import unittest

# import siscompleter from the ../bettersis folder
curr_dir = os.path.realpath(os.path.dirname(__file__))
bettersis_path = os.path.join(curr_dir, "..", "bettersis")
sys.path.insert(1, os.path.realpath(bettersis_path))
import siscompleter


class TestSiscompleter(unittest.TestCase):
    """
    Tests siscompleter.py
    """

    def test_production(self):
        """
        Makes sure that we are in production mode.
        """
        self.assertFalse(siscompleter.boold, "boold should be False in production mode")

    def test_get_files(self):
        """
        Tests the get_files() function.
        """
        files = siscompleter.get_files()
        for file_param in files.keys():
            self.assertIsNone(files[file_param], "files don't have sub-parameters")
            self.assertEqual(type(file_param), str, "files should be strings")

    def test_get_folders(self):
        """
        Tests the get_folders() function.
        """
        folders = siscompleter.get_folders()
        for folder_param in folders.keys():
            self.assertIsNone(folders[folder_param], "folders don't have sub-parameters")
            self.assertEqual(type(folder_param), str, "folders should be strings")

    def test_get_act_map_params(self):
        """
        Tests the get_act_map_params() function.
        """
        params = siscompleter.get_act_map_params()

        stack = list(params.items())
        visited = set()
        while stack:
            k, v = stack.pop()
            if isinstance(v, dict):
                if k not in visited:
                    stack.extend(v.items())
            else:
                self.assertIsNone(v, "the sub-parameter has to be None (or a dictionary)")
                self.assertEqual(type(k), str, "parameter should be a string")

            visited.add(k)

    def test_get_read_blif_params(self):
        """
        Tests the get_read_blif_params() function.
        """
        params = siscompleter.get_read_blif_params()

        stack = list(params.items())
        visited = set()
        while stack:
            k, v = stack.pop()
            if isinstance(v, dict):
                if k not in visited:
                    stack.extend(v.items())
            else:
                self.assertIsNone(v, "the sub-parameter has to be None (or a dictionary)")
                self.assertEqual(type(k), str, "parameter should be a string")

            visited.add(k)

    def test_get_read_eqn_params(self):
        """
        Tests the get_read_eqn_params() function.
        """
        params = siscompleter.get_read_eqn_params()

        stack = list(params.items())
        visited = set()
        while stack:
            k, v = stack.pop()
            if isinstance(v, dict):
                if k not in visited:
                    stack.extend(v.items())
            else:
                self.assertIsNone(v, "the sub-parameter has to be None (or a dictionary)")
                self.assertEqual(type(k), str, "parameter should be a string")

            visited.add(k)

    def test_get_commands(self):
        """
        Tests the get_commands() function.
        """
        commands = siscompleter.get_commands()

        stack = list(commands.items())
        visited = set()
        while stack:
            k, v = stack.pop()
            if isinstance(v, dict):
                if k not in visited:
                    stack.extend(v.items())
            else:
                self.assertIsNone(v, "the sub-parameter has to be None (or a dictionary)")
                self.assertEqual(type(k), str, "parameter should be a string")

            visited.add(k)

    def test_get_source_params(self):
        """
        Tests the get_source_params() function.
        """
        params = siscompleter.get_source_params()

        for param in params.keys():
            self.assertIsNone(params[param], "params don't have sub-parameters")
            self.assertEqual(type(param), str, "param should be strings")


if __name__ == "__main__":
    unittest.main()
