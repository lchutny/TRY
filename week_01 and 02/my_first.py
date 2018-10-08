# input size as x
x = int(input("Enter an integer for the size of the square"))
# assign row=x
row = x
#row loop
while row > 0:
    #assign col=x
    col = x
    #column loop
    while col >0:
        if col%2 == 0:
            print("__", end=" ")
        else:
            print("$$", end=" ")
        col -=1
    print("")
    row -=1
