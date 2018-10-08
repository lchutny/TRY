n = int(input("Enter a board size: "))

#error checking for zero/ negative number entries
while n <= 0:
    print("Incorrect entry, please enter a number > 0.")
    n = int(input("Enter a board size: "))

#instantiate dictionary with all the unique (i,j) as keys and zero as the value for each key
board = {(i,j):0 for i in range (0,n) for j in range (0,n)}
#place special value for first column, j=0 as '1' as you have no right turns to get there, so always 1
for i in range(0,n):
    board[i,0] = 1

#start point is (i,j) as (row,column) index = (0,0)
i,j = (0,0) #tuple for row/column, zero at start #DO WE NEED THIS??

#loop on i (row number) from 0 to n
for i in range (0, n-1):
    #loop on j (column number) from 1 to n (because column '0' is already filled)
    for j in range(1,i+1):
        board[(i+1,j)]=board[(i,j)]+board[(i,j-1)]
        print("i,j = ", i,",",j,"   board(i+1,j) = ",board[(i+1,j)])

# #print board:
for i in range(0,n):
    for j in range (0,n):
        print(board[i,j],end=' ')
    print('')
