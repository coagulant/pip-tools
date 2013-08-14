# coding: utf-8
import sys

if sys.version_info[0] < 3:
    string_types = basestring,
else:
    string_types = str,
