#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except (Exception) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        result None
    else:
        return res
