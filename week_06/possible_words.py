
""" Determine all possible combinations of words. Return a list of all unique possible words from 2-7 letters.
"""
from sys import argv
import itertools as it
import operator
import time
import string

rack = 'y*'
tups = []
for n in range(2,len(rack)+1):
    y=list(it.permutations(rack, n)) # Returns list of tuples - each tuple is a 'word'.
    tups += y
words=[]
for tup in tups:
    words.append(''.join(tup)) # Convert list of tuples to list of words.

# List 'words' still contains wildcards. If there is a wildcard in the rack, replace each wildcard with each letter of the alphabet
if '*' in rack or '?' in rack:
    wildcard_words = []
    for word in words:
        if '*' in word:
            for let in string.ascii_lowercase:
                new_word = word.replace('*',let)
                wildcard_words.append(new_word)

        elif '?' in word:
            for let in string.ascii_lowercase:
                new_word = word.replace('?',let)
                wildcard_words.append(new_word)
words += wildcard_words

# Now need to remove any words that have wildcards:
clean_words = []
for word in words:
    if '*' not in word and '?' not in word:
        clean_words.append(word)

# Make words a set to get unique words, then make a list again.
clean_words = list(set(clean_words))
print(clean_words)
print(len(clean_words))
