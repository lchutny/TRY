def weighted_avg(grades,weights):
    #initialize variables
    sumwt = 0
    wtdavg = 0
    n=0

    #Check that the two lists are the same length before continuing
    if len(weights) != len(grades):
        raise Exception("Number of weight and grade entries must be equal")

    for g in grades: #loop through the grades
        #add the contribution from each grade to the weighted average
        wtdavg += g/100*weights[n]
        #sum the weights to check they equal 100
        sumwt += weights[n]
        # check that each g is >= 0 and raise exception if so
        if g < 0:
            raise Exception("No grades can be less than zero")
            break
        #Check for weights outside bounds
        elif weights[n] < 0 or weights[n] > 100:
            raise Exception("Weight(s) greater than 100 or less than zero, incorrect input")
            break
        n += 1

    #Check that the sum of the weights equal 100
    if sumwt != 100:
        raise Exception("Weights do not sum to 100")

    return wtdavg

grades1 = [88,99,100,70]
weights1 = [30, 30, 30, 5]

grades2 = [78, 75, 80, 99]
weights2 = [110, 10, -20, 0]

grades3 = [84, 80, 67, 97]
weights3 = [50, 25, 25]

grades4 = [100, 80, 90, 75]
weights4 = [20, 25, 25, 30]

# print(weighted_avg(grades1,weights1))
# print(weighted_avg(grades2,weights2))
# print(weighted_avg(grades3,weights3))
print(weighted_avg(grades4,weights4))
