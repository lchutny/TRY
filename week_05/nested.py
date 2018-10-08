#example of floor division

def sum_digits(x):
    result = abs(x)
    sumx = 0
    while result >0:
        sumx += result%10
        result = result//10
    return sumx

def diff_sum_digits(x):
    return abs(x-sum_digits(x))

def wraps_diff_sum_digits(x):
    y = x
    while y >= 10:
        y = diff_sum_digits(y)
    else:
        return y

print(sum_digits(54321) == 15)
print(sum_digits(-54321) == 15)
print(diff_sum_digits(54321) == 54306)
print(wraps_diff_sum_digits(54321) == 9)
