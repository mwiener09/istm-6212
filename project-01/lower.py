#!/usr/bin/env python

"""
Transform each line of a text to lower case.
"""

import fileinput

def process(line):
    """For each line of input, print each line in all lower case letters."""
    print(line.lower().strip())

for line in fileinput.input():
    process(line)