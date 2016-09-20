#!/usr/bin/env python

"""
Transform each line of a text to lower case.
"""

import fileinput
from stop_words import get_stop_words
import string


def format_stopwords():
# import list of stop words, remove punctuation and lower-case as to match list of words in little women
    stop_words = get_stop_words('english')
    
        
    stop_words_np = []
    for word in stop_words:
        word = word.lower()
        stop_words_np.append(word)
    return stop_words_np


def process(line, stop_words_np):
    """For each line of input, print each line in all lower case letters."""
    w = line.lower().strip()
    if len(w) == 1:
        pass
    
    elif not w in stop_words_np:
        print(w)

for line in fileinput.input():
    stopwords = format_stopwords()
    process(line, stopwords)