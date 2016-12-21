# Utilities related to prime numbers, to be reused among problems

from itertools import islice
from itertools import count
from math import sqrt

# Checks whether n is prime or not (using Rabin-Miller)
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    if n % 5 == 0: return False

    ar = [2, 3]
    for i in ar:
        if _witness(i, n): return False
    return True

def _witness(a, n):
    t = 0
    u = n-1
    while u&1 == 0:
        t += 1
        u = u >> 1

    xi1 = _modular_exp(a, u, n)
    xi2 = 0

    for i in range(0, t):
        xi2 = xi1 * xi1 % n
        if (xi2 == 1) and (xi1 != 1) and (xi1 != (n-1)): return True
        xi1 = xi2
    if xi1 != 1: return True
    return False

def _modular_exp(a, b, n):
    d = 1
    k = 0
    while b>>k > 0:
        k += 1

    for i in range(k-1, -1, -1):
        d = d*d%n
        if ((b>>i) & 1) > 0: d = d*a%n
    return d


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
