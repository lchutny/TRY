#output row of Pascal's triangle given row number, starting at 1
#use a list of lists to represent the triangle

#get n
rownum = int(input("Enter row number of Pascal's triangle: "))
if rownum <= 0:
    print("Must have positive nonzero input. Start again")
else:
    #put first two rows into triangle
    triangle = [[1],[1,1]]
    #row number counter, NOT index
    n=3

    #populate triangle row
    while n <= rownum:
        #populate triangle row as appropriate sized list
        row=[None]*(n)
        #populate first and last items in row
        row[0]=1
        row[n-1]=1
        #populate middle elements of row (sums)
        x = 1
        while x < n-1:
            row[x] = triangle[n-2][x-1]+triangle[n-2][x]
            x +=1
        triangle.append(row)
        n+=1

    print(*triangle[rownum-1], sep=' ')
