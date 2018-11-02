""" Main Scrabble Game program """


from sys import argv, exit
import itertools as it
import operator
import time
import string

import score_word    # my score_word function

start = time.time()
def possible_words(letters):
    """ Determine all possible combinations of words. Return a list of all unique possible words from 2 to max 7 letters.
    """
    tups = []
    for n in range(2,len(letters)+1):
        y=list(it.permutations(letters, n)) # Returns list of tuples - each tuple is a 'word'.
        tups += y
    words=[]
    for tup in tups:
        words.append(''.join(tup)) # Convert list of tuples to list of words.

    words = list(set(words))
    return words

def valid_word(word,wordlist):
    """ Review a word against given list of acceptable words. Return true or false.
    """
    # Set the valid word flag to false and check the word against the list.
    is_valid = False
    if word in wordlist:
        is_valid = True
    return is_valid

# Get letter rack from Keyboard as program is called from command line. Error
# check for empty rack, too many characters or non letter/wildcard characters.
try:
    rack = argv[1].lower()
    pass
except Exception as e:
    print("Input error - empty rack. Please try again")
    exit(1)
if not rack.count('*') > 1 and not rack.count('?') > 1 and not len(rack) > 7:
    for let in rack:
        if let in string.ascii_lowercase or let == '*' or let == '?':
            pass
        else:
            print("Input must be letters or * or ? only.")
            exit(1)
else:
    raise Exception("Input must be only letters or wildcards * and ?. Only 1 each of * and ? are allowed - maximum 2 wildcards total.")

# no_wild_rack = ''.join([let for let in rack if let in string.ascii_lowercase])


# Get list of valid words from text file and error check if error getting file:
try:
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        scrabble_words = [datum.strip('\n').lower() for datum in raw_input]
        print(scrabble_words)
except Exception as e:
    print("Scrabble word dictionary import failed", e)
    exit(1)

# Create words with all combinations of letters/symbols
rack_words = possible_words(rack)
rack_words.sort(reverse=True)  # Sort list of possible word
rack_words = list(set(rack_words))

whole_list = []
# Score words including wild cards.
for word in rack_words:
    wordscore = score_word.score_word(word)
    scoretup = (wordscore,word)
    whole_list.append(scoretup)

# Sort the whole_list first by reverse alphabetical order of words
whole_list.sort(key=operator.itemgetter(1),reverse=True)
# Then sort the whole_list by score.
whole_list.sort(key=operator.itemgetter(0),reverse=True)

valid_list = []

# Now replace each wild card (if present) and validate
for elem in whole_list:
    wild_words = []
    if '*' in elem[1] and '?' in elem[1]:
        for let in string.ascii_lowercase:
            word = elem[1].replace('*',let)
            for let in string.ascii_lowercase:
                word2 = word.replace('?',let)
                wild_words.append(word2)
    elif '*' in elem[1]:
        for let in string.ascii_lowercase:
            word = elem[1].replace('*',let)
            wild_words.append(word)
    elif '?' in elem[1]:
        for let in string.ascii_lowercase:
            word = elem[1].replace('?',let)
            wild_words.append(word)
    else:
        if valid_word(elem[1],scrabble_words):
            valid_list.append(elem)
    wild_words=list(set(wild_words))
    print("wildwords")
    print(wild_words)
    for w3 in wild_words:
        if valid_word(w3,scrabble_words):
            newtup = (elem[0],word2)
            valid_list.append(newtup)

valid_list = list(set(valid_list))
#checking if no valid words:
if not valid_list:
    print("No valid words could be found")
    exit(1)

# valid_list should now contain unique tuples of scores of all valid words
# Sort the list first by reverse alphabetical order of words
valid_list.sort(key=operator.itemgetter(1),reverse=True)
# Then sort the final list by score.
valid_list.sort(key=operator.itemgetter(0),reverse=True)

# Print in way that matches assignment requirements.
for n in range(0,len(valid_list)):
    print(f"({valid_list[n][0]}, {valid_list[n][1]})")
print("Total number of words: ", len(valid_list))

end = time.time()
print(f"running time = {(end-start):.5} seconds")
