#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST_TEXTEDITOR: tests texteditor.py
"""

__author__ = "Zenaro Stefano"
__version__ = "2021-03-05 1.0.0"

import os
import sys
import unittest

# import texteditor from the ../bettersis folder
curr_dir = os.path.realpath(os.path.dirname(__file__))
bettersis_path = os.path.join(curr_dir, "..", "bettersis")
sys.path.insert(1, os.path.realpath(bettersis_path))
import texteditor


class TestText:
    """
    Creates a text object to test SisLexer.
    """
    def __init__(self, line):
        self.lines = [line]


class TestLexer(unittest.TestCase):
    """
    Tests the SisLexer() class of texteditor.py
    """
    def test_model(self):
        """
        Tests .model lexer.
        """
        lexer = texteditor.SisLexer()
        testtext = TestText(".model test")

        chars_prop = lexer.lex_document(testtext)(0)

        # "." blue
        char_color = chars_prop[0][0]
        char = chars_prop[0][1]
        self.assertEqual("DeepSkyBlue", char_color)
        self.assertEqual(".", char)

        # "m" blue
        char_color = chars_prop[1][0]
        char = chars_prop[1][1]
        self.assertEqual("DeepSkyBlue", char_color)
        self.assertEqual("m", char)

        # "o" blue
        char_color = chars_prop[2][0]
        char = chars_prop[2][1]
        self.assertEqual("DeepSkyBlue", char_color)
        self.assertEqual("o", char)

        # "d" blue
        char_color = chars_prop[3][0]
        char = chars_prop[3][1]
        self.assertEqual("DeepSkyBlue", char_color)
        self.assertEqual("d", char)

        # "e" blue
        char_color = chars_prop[4][0]
        char = chars_prop[4][1]
        self.assertEqual("DeepSkyBlue", char_color)
        self.assertEqual("e", char)

        # "l" blue
        char_color = chars_prop[5][0]
        char = chars_prop[5][1]
        self.assertEqual("DeepSkyBlue", char_color)
        self.assertEqual("l", char)

        # " "
        char_color = chars_prop[6][0]
        char = chars_prop[6][1]
        self.assertEqual(" ", char)

        # "t" white
        char_color = chars_prop[7][0]
        char = chars_prop[7][1]
        self.assertEqual("White", char_color)
        self.assertEqual("t", char)

        # "e" white
        char_color = chars_prop[8][0]
        char = chars_prop[8][1]
        self.assertEqual("White", char_color)
        self.assertEqual("e", char)

        # "s" white
        char_color = chars_prop[9][0]
        char = chars_prop[9][1]
        self.assertEqual("White", char_color)
        self.assertEqual("s", char)

        # "t" white
        char_color = chars_prop[10][0]
        char = chars_prop[10][1]
        self.assertEqual("White", char_color)
        self.assertEqual("t", char)


if __name__ == "__main__":
    unittest.main()
