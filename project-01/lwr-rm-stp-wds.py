#!/usr/bin/env python

"""
Exclude stop words from a list of words, transform each line of a text to lower case.
"""

import fileinput
from stop_words import get_stop_words
import string

def format_stopwords():
    """Function to import list of stop words and lower-case them."""
    stop_words = get_stop_words('english')
    stop_words_lw = []
    for word in stop_words:
        word = word.lower()
        stop_words_lw.append(word)
    return stop_words_lw

def process(line, stop_words_lw):
    """For each line of input, print each line in lower-case, exclude one character words."""
    w = line.lower().strip()
    if len(w) == 1:
        pass
    elif not w in stop_words_lw:
        print(w)

for line in fileinput.input():
    stopwords = format_stopwords()
    process(line, stopwords)
