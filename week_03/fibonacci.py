# Gets an integer input and returns all Fibonacci numbers less than or equal to the input in order

#typecast as integer just in case
inputint = int(input("Calculating Fibonacci sequence. Please enter an integer for maximum: "))
#ensure positive number
num = abs(inputint)
#create list with first two Fibonacci numbers:
fibs = [1,1]

#start creating list at index 2
n = 2
newnum = 1
while fibs[n-1] <= num:
    #calculate new number in sequence
    newnum = fibs[n-1]+fibs[n-2]
    #break out of loop if next value would be bigger than input
    if newnum > num:
        break
    #append new number to end of list and continue otherwise
    else:
        fibs.append(newnum)
        n+=1
print(*fibs,sep = ' ')
