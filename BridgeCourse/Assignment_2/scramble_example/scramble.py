# Script module to scramble a phrase

def interleave(A,B):
    """ Function that takes two strings of same lengths and interleaves
    them, returning the interleave string"""

    interleaf = []

    if len(A) != len(B):
        print("Strings must be equal length")
        return interleaf
    else:
        for n in range(0,len(A)):
            interleaf.append(A[n])
            interleaf.append(B[n])
        return interleaf

def is_power_of_two(n):
    # Bitwise AND to check power of 2, returns True or False
    #assumes non-negative integer input
    return bool(n and not (n & (n - 1)))

# Recursive mix:
def mix(string_in):
    #base case:
    if len(string_in) == 2:
        return string_in
    else:
        x = len(string_in)
        half1 = string_in[0:int(x/2)]
        half2 = string_in[int(x/2):x]
        return "".join(interleave(mix(half1),mix(half2)))

# Get phrase from text file; store in a list
inputlist = []
with open('input.txt','rt') as filein:
    inputstring = filein.read()
inputlist = inputstring.split('\n') # List of phrases, one per list entry

outputlist = []  # For writing to file at end

for n in range(0, len(inputlist)-1):
    if len(inputlist[n]) <= 1:
        outputlist[n] = 'EMPTY INPUT, not scrambled'
    else:
        # Check if phrase length is power of 2. If not, add .. until it is.
        x = len(inputlist[n])
        if is_power_of_two(x):
            pass
        else:
            y = x
            while not is_power_of_two(y):
                inputlist[n] += '.'
                y = len(inputlist[n])
        #Now use recursion to scramble the string by halves
        outputlist.append(mix(inputlist[n]))

#print(*outputlist, sep = '\n')

# Print the output to a text file
with open ('outputlc.txt', 'wt') as fileout:
    for line in outputlist:
        print(line, file = fileout, sep='\n')
