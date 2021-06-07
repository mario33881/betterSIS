#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST_ALL: runs all the unit tests inside the tests folder
"""

import unittest

try:
    from .test_bettersis import *
    from .test_siscompleter import *
    from .test_texteditor import *
    from .test_update_checker import *

except ImportError:
    from test_bettersis import *
    from test_siscompleter import *
    from test_texteditor import *
    from test_update_checker import *

if __name__ == "__main__":
    unittest.main()
