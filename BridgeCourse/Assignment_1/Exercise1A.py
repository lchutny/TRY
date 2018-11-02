# #Get number of Prime Factors for a number input by user
import math

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

#Number of prime factors:
big = 1234567890 # Number to find factors for.

def primes_up_to(n):
    """Generates all primes less than n. Sieve of Erastothenes; courtesy
        David Eppstein, UC Irvine, 28 Feb 2002, faster code by Mike Dell'Amico
    """
    if n <= 2: return
    yield 2
    F = [True] * n
    seq1 = range(3, int(math.sqrt(n)) + 1, 2)
    seq2 = range(seq1[-1] + 2, n, 2)
    for p in filter(F.__getitem__, seq1):
        yield p
        for q in range(p * p, n, 2 * p):
            F[q] = False
    for p in filter(F.__getitem__, seq2):
        yield p

def numfact(big):
    #Now check big to see if those primes are Factors
    count = 0
    uniquefact = []
    for n in range(2, big):
        if big % n == 0:
            if is_prime(n):
                count +=1
                uniquefact.append(n)
            while big % n == 0:
                big = big/n
        if int(big) == 1:
            break  #stop when the divisor is 1
    return (count, uniquefact)

# Check if number itself is prime:
if is_prime(big):
    print ("Number is prime, so has only 1 unique prime factor, itself")
else:
    unique_factors = numfact(big)
    print ("%s has %s unique prime factors" %(big,unique_factors[0]))
    print("Those are: ", unique_factors[1])
