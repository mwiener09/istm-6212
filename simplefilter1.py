#!/usr/bin/env python

"""
A filter that separates each word of a document into its own line.
"""

import fileinput
import string

def process(line):
    """For each line of input, split words into rows and strip punctuation."""
    for word in line.split():
        for c in string.punctuation:
            word= word.replace(c,"")
        print(word.strip())
        


for line in fileinput.input():
    process(line)
