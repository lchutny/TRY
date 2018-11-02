import string
from sys import argv, exit
import itertools as it
import operator
import time
import collections

import score_word

start = time.time()

whole_list = [('apple', 8),('king',7), ('ae',2)]
whole_list.sort(key=operator.itemgetter(1))
whole_list = dict(whole_list)
print(whole_list)

word = 'apple'
wordscore = 9
scoretup = (word,wordscore)

if word in whole_list:
    found_score = whole_list.get(word)
    if found_score < wordscore:
        whole_list.pop(word)
        whole_list[word] = wordscore
else:
    whole_list[word] = wordscore

print(whole_list)

final_list = []
for word in whole_list:
    wordsc = whole_list.get(word)
    scoretup2 = (wordsc,word)
    final_list.append(scoretup2)

final_list.sort(key=operator.itemgetter(1),reverse=True)
# Then sort the whole_list by score.
final_list.sort(key=operator.itemgetter(0),reverse=True)

print(final_list)



end = time.time()
print(f"running time = {(end-start):.5} seconds")
