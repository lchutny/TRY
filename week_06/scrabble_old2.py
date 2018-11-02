""" Main Scrabble Game program """


from sys import argv, exit
import itertools as it
import operator
import time
import string

import score_word    # my score_word function

"""NEED TO ADD: ERROR CHECKING (). Test in different OSs"""

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

no_wild_rack = ''.join([let for let in rack if let in string.ascii_lowercase])



# Get list of valid words from text file and error check if error getting file:
try:
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        scrabble_words = [datum.strip('\n').lower() for datum in raw_input]
except Exception as e:
    print("Scrabble word dictionary import failed", e)
    exit(1)

# Create words with no wild cards (only action if there are no wildcards)
rack_words = possible_words(no_wild_rack)
rack_words.sort(reverse=True)  # Sort list of possible word

# Now compare the no wild card words to the word list using the valid_word
# function and create the new list of scored valid words from the rack_words.
final_list = []
for word in rack_words:
    if valid_word(word,scrabble_words):
        wordscore = score_word.score_word(word)
        scoretup = (wordscore,word)
        final_list.append(scoretup)

# final_list currently has scored valid words without wildcards

# Create words from rack with wildcards:
if '*' in rack or '?' in rack:
    if '?' in rack:
        new_rack = rack.replace('?','*') # Replace ? by * to simplify
    else:
        new_rack = rack

    # Create possible words containing wildcards:
    for let in string.ascii_lowercase:
        word = rack.replace('*',let)
        if valid_word(word,scrabble_words):
            wordscore = score_word.score_word(word)
            scoretup = (wordscore,word)
            final_list.append(scoretup)

# If both wildcards are there we have to double loop:
elif '?' and '*' in rack:
    for let in string.ascii_lowercase:
        word = rack.replace('*',let)
        for let in string.ascii_lowercase:
            word = rack.replace('?',let)
            if valid_word(word,scrabble_words):
                wordscore = score_word.score_word(word)
                scoretup = (wordscore,word)
                final_list.append(scoretup)

#checking if no valid words:
if not final_list:
    print("No valid words could be found")
    exit(1)

# final_list should now contain tuples of scores of all valid words
# Sort the list first by reverse alphabetical order of words
final_list.sort(key=operator.itemgetter(1),reverse=True)
# Then sort the final list by score.
final_list.sort(key=operator.itemgetter(0),reverse=True)

# Print in way that matches assignment requirements.
for n in range(0,len(final_list)):
    print(f"({final_list[n][0]}, {final_list[n][1]})")
print("Total number of words: ", len(final_list))

end = time.time()
print(end-start)
