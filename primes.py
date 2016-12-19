# Utilities related to prime numbers, to be reused among problems

from itertools import islice
from itertools import count
from math import sqrt

# Checks whether n is prime or not
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
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
            for j in range(3*i+1, sieve_dim, 2*i+1):
                sieve[j] = True
    return primes


# Returns the prime factors of n.
# If n is prime, it returns an empty list.
# It takes a precomputed sieve
def prime_factors(n, precomputed_sieve = None):

    primes = precomputed_sieve

    # Limit the sieve to be made
    if primes == None:
        limit = n
        if n%2 == 0:
            limit = int(n/2)
        elif n%3 == 0:
            limit = int(n/3)
        elif n%5 == 0:
            limit = int(n/5)

        primes = sieve_of_eratosthenes(limit)

    remain = n
    prime_factors = []

    for prime in primes:
        if prime * prime > n:
            prime_factors.append(remain)
            return prime_factors

        pf = False
        while remain % prime == 0:
            pf = True
            remain = remain / prime

        if pf == True:
            prime_factors.append(prime)

        if remain == 1:
            return prime_factors

    return prime_factors
