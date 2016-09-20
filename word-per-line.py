#!/usr/bin/env python

"""
A filter that separates each word of a document into its own line.
"""

import fileinput
import re

def process(line):
    """For each line of input, split words into rows and strip punctuation."""
    line = re.findall(r'\w+',line)
    for word in line:
        print(word.strip())

for line in fileinput.input():
    process(line)