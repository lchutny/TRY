#output row of Pascal's triangle given row number, starting at 1
#use a list of lists to represent the triangle

#get n
rownum = int(input("Enter row number of Pascal's triangle: "))
if rownum <= 0:
    print("Must have positive nonzero input. Start again")
else:
    #put first two rows into triangle
    triangle = [[1],[1,1]]
    n=2

    #populate triangle row
    while n < rownum:
        #populate triangle row as appropriate sized list
        y=n+1
        row=[None]*(y)
        #populate first and last items in row
        row[0]=1
        row[n]=1
        #populate middle elements of row (sums)
        x = 1
        while x < n:
            row[x] = triangle[n-1][x-1]+triangle[n-1][x]
            x +=1
        triangle.append(row)
        n+=1

    print(*triangle[rownum-1], sep=' ')
