def best(score,names):
    #initialize local variables
    totscore = 0
    winner = ''
    #loop through names to find one with best score per the rules indicated
    for name in names:
        currentnamescore = score(name)
        if currentnamescore > totscore:
            totscore = currentnamescore
            winner = name
        elif currentnamescore == totscore: #report only the first in the list with the highest score
            continue
    return winner #return winner's name

def len_score(name):
    score = len(name)
    return score

def number_of_vowels(word):
    vowel_score = 0
    for l in word:
        if l.lower() in 'aeiou':
            vowel_score += 1
    return vowel_score

#f = reduce(lambda x,l: (x + 1) if l == 'a')

# def a_s(word):
#     score = 0
#     for l in word:
#         if l.lower() == 'a':
#             score += 1
#     return score

names = ["Ben", "April", "Zaber", "Alexiaa", "McJagger", "J.J.", "Madonna"]
# print(f"{best(len_score,names)} has the longest name.")
# print(f"{best(number_of_vowels,names)} has the most vowels.")
# f = lambda name: sum([1 for x in name if x=='a'])
# print(f"Anna has {f('anna')} a's")

print(f"{best((lambda name: sum([1 for x in name if x=='a'])),names)} has the most a's.")
