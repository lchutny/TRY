# Primes try out
import math

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

primes = []
plist = primes_up_to(3000)
for x in plist:
    primes.append(x)
print(primes)

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

# yes = is_prime(13717421)
# print(yes)
