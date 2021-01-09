#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from ._version import __version__
    from .bettersis import Bettersis

except ImportError:
    from _version import __version__
    from bettersis import Bettersis
