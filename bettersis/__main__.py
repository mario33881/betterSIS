#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Imports modules and packages for the user that executes:
python -m bettersis
"""

from ._version import __version__  # noqa: F401

try:
    from . import bettersis

except ImportError:
    from .bettersis import bettersis

if __name__ == "__main__":
    bettersis.main()
