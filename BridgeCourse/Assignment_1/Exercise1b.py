#Write a script that prompts the user for their phone number, x. Then carry out the following steps:
#
#
# 1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)
# 2. Compute the sum of the digits of y, and store the result back in y.
# 3. Repeat step 2 until y has just one digit, then display it.
#
# What answer do you get?

def sum_digits(x):
    result = abs(x)
    sumx = 0
    while result >0:
        sumx += result%10
        result = result//10
    return sumx


phone_number = int(input("Please enter your phone number as 10 digits (1234567890): "))

y = phone_number - sum_digits(phone_number)
print(sum_digits(phone_number))
print(y)
while y > 9:
    y = sum_digits(y)
    print(y)

print("y =", y)
