# Utilities related to prime numbers, to be reused among problems

from itertools import islice
from itertools import count
from math import sqrt

# Checks whether n is prime or not
def is_prime(n):
    if n < 2 or n % 2 == 0: return False
    if n == 2 or n == 3: return True
    return all(n%i for i in islice(count(3,2), int(sqrt(n)-1)))


# Find all prime numbers up to n using the sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    # List of only half+1 the numbers below n (odd numbers + 2)
    # Mark all odd numbers as primes at the beginning
    sieve_dim = int((n-1)/2+1)
    sieve = [False]*sieve_dim
    sieve[0] = True
    primes = [2]
    for i, isComposite in enumerate(sieve):
        if isComposite == False:
            primes.append(2*i+1)
            for j in xrange(3*i+1, sieve_dim, 2*i+1):
                sieve[j] = True
    return primes


# Returns the prime factors of n
def prime_factors(n):
    primes=sieve_of_eratosthenes(int(sqrt(n)))
    prime_factors = []
    for i in primes:
        if n%i == 0:
            prime_factors.append(i)
    return prime_factors

