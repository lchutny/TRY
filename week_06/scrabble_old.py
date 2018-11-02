""" Main Scrabble Game program """


from sys import argv
import itertools as it
import operator
import time
import string

import score_word    # my score_word function

"""NEED TO ADD: ERROR CHECKING (nonascii, quotes on word in input, no valid words, only non letters) AND wildcard characters. Test in different OSs"""

#start = time.time()
def possible_words(rack):
    """ Determine all possible combinations of words. Return a list of all unique possible words from 2-7 letters.
    """
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
            elif '*' and '?' in word:
                for let in string.ascii_lowercase:
                    new_word1 = word.replace('*', let)
                    for let in string.ascii_lowercase:
                        new_word = new_word1.replace('?', let)
                        wildcard_words.append(new_word)
    words += wildcard_words

    # Now need to remove any words that have wildcards:
    clean_words = []
    for word in words:
        if '*' not in word and '?' not in word:
            clean_words.append(word)
    # Make words a set to get unique words, then make a list again.
    clean_words = list(set(clean_words))
    return clean_words

def is_valid_word(rack_words):
    """Review rack_words against list of acceptable words: sowpods.txt. Return new word list that only contains valid words.
    """
    # Get the acceptable word list.
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        scrabble_words = [datum.strip('\n').lower() for datum in raw_input]
    # Set the valid word list to empty and check the words against the list.
    valid_words = []
    for word in rack_words:
        if word in scrabble_words:
            valid_words.append(word)
    return valid_words

# Get letter rack from Keyboard as program is called from command line.
rack = argv[1].lower()
rack_words = []

# Get the possible unique words and sort them for faster review.
rack_words = possible_words(rack)
rack_words.sort()  # rack_words now a sorted list of all possible combinations.

# Now compare the words to the word list using the is_valid_word function and
# create the new list of valid words from the rack_words. Sort this list in
# reverse order to get right output
valid = []
valid = is_valid_word(rack_words)
valid.sort(reverse=True)

# For each word in valid list, call score_word.py to score the word,
# store result as a list of tuples of (word,score).
scored_valid = []
for word in valid:
    wordscore = score_word.score_word(word)
    scoretup = (wordscore,word)
    scored_valid.append(scoretup)

# Sort the scored list by score.
scored_valid.sort(key=operator.itemgetter(0),reverse=True)

# Print in way that matches assignment requirements.
for n in range(0,len(scored_valid)):
    print(f"({scored_valid[n][0]}, {scored_valid[n][1]})")
print("Total number of words: ", len(scored_valid))

#end = time.time()
#print(end-start)
