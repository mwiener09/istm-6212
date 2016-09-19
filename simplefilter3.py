#!/usr/bin/env python

"""
Transform each line of a text to lower case.
"""

import fileinput
from stop_words import get_stop_words
#from nltk.corpus import stopwords

stop_words = set(get_stop_words('english'))
   
print(stop_words)

def process(line):
    """For each line of input, print each line in all lower case letters."""
    w = line.lower().strip()
    
    if not w in stop_words:
        print(w.strip())

for line in fileinput.input():
    process(line)