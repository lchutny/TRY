def is_consonant(char):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    if char.lower() in consonants:  #could have used 'not in 'aeiou''
        return True
    else:
        return False

def to_piglatin(words):
    #reuse code from Week3 in general
    wordsin = words.split(' ')
    #if sentence, split period off end
    if len(wordsin)>1:
        last_index=len(wordsin)-1
        wordsin[last_index] = wordsin[last_index][:-1]
    wordsout=[]
    #loop through each word
    for word in wordsin:
        endstr = [] #create a string for the final consonants
        count = 0 #count how many consonants we cut so we know where to slice the root of the word
        #while i in word is is_consonant(i) (while loop wouldn't work - not sure why):
        for i in word:
            if is_consonant(i):
                endstr.append(i)
                count +=1
            else:
                break
        endword = str(word[count:]).lower()+''.join(endstr).lower()+'ay'
        wordsout.append(endword) #all words in lower case
    #capitalize first word
    wordsout[0] = wordsout[0][0].upper() + wordsout[0][1:]
    #check for sentence, add period
    if len(wordsout)>1:
        wordsout.append('.')

    return ' '.join(wordsout) #I have an extra space at end of sentence. Would need to fix that for 100%



print(to_piglatin('CAR'))
