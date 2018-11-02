""" Main Scrabble Game program"""


from sys import argv, exit
import itertools as it
import operator
import time
import string

import score_word    # my score_word function

start = time.time()

def process_words(scrabble_words, length):
    """ Take given list of acceptable scrabble words and remove words longer than number of letters in rack"""
    new_scrabble_words=[]
    for word in scrabble_words:
        if len(word) <= length:
            new_scrabble_words.append(word)
    return list(set(new_scrabble_words))

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

# Get list of valid words from text file and error check if error getting file:
try:
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        orig_scrabble_words = [datum.strip('\n').lower() for datum in raw_input]
except Exception as e:
    print("Scrabble word dictionary import failed", e)
    exit(1)

# Process Dicionary to remove useless clutter
scrabble_words = process_words(orig_scrabble_words, len(rack))
scrabble_words = sorted(scrabble_words)
whole_list = []

# Look at each word in dictionary and see if it can be made with the rack
for word in scrabble_words:  # Featuring our shortened list
    tryrack = list(rack)
    toscore = []
    possible = True
    while possible:
        for let in word:
            if let in tryrack:
                tryrack.remove(let)
                toscore.append(let)
            elif '*' in tryrack:
                tryrack.remove('*')
                toscore.append('*')
            elif '?' in tryrack:
                tryrack.remove('?')
                toscore.append('?')
            else:
                possible = False
                break
        if possible:
            wordscore = score_word.score_word(''.join(toscore))
            scoretup = (wordscore,word)
            if scoretup[1] in whole_list:
                if scoretup[0] > whole_list[]
                whole_list.append(scoretup)

whole_list = list(set(rack_words)) # Ensure uniqueness


# Sort the whole_list first by reverse alphabetical order of words
whole_list.sort(key=operator.itemgetter(1),reverse=True)
# Then sort the whole_list by score.
whole_list.sort(key=operator.itemgetter(0),reverse=True)


if not rack_words:
    print("No valid words could be found")
    exit(1)

# Print in way that matches assignment requirements.
for n in range(0,len(whole_list)):
    print(f"({whole_list[n][0]}, {whole_list[n][1]})")
print("Total number of words: ", len(whole_list))

end = time.time()
print(f"running time = {(end-start):.5} seconds")
