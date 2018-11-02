#Get number of Prime Factors for a number input by user
def is_prime(n):
#to determine if a number is prime or not
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range (2,n):
            if(n % x == 0):
                return False
        return True

def primes(big):
    prime_list = []
    for n in range(2,big):
        if is_prime(n):
            prime_list.append(n)
    return prime_list

def numfactors(big):
    prime_list = primes(big)
    count = 0
    for n in prime_list:
        if big % n == 0:
            count +=1
    return count

# big = int(input("Enter value to find number of prime factors for: "))
# big_abs = abs(big) #if number is negative, make positive
big = 1234567890
if big == 0 or big == 1:
    print ("Number must not be zero or 1, try again")
else:
    if is_prime(big_abs):
        print ("Number is prime, so has only 1 unique prime factor, itself")
    else:
        unique_factors = numfactors(big_abs)
        print ("%s has %s unique prime factors" %(big,unique_factors))
