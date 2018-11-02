def score_word(word):
    """ Score word using Scrabble standard letter scores and 0 for wildcards ? and * .  Assumes error catching for incorrect characters done in calling program.
    """
    word_score = 0
    # Score table provided by instructors.
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    # Loop through the letters in the word and add each letter's score to the total
    for letter in word:
        if letter == '?' or letter == '*':
            letscore = 0
        else:
            letscore = scores.get(letter.lower()) #ensure letters are lower case
        word_score += letscore
    return word_score  # Return the word score
