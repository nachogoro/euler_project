#!/usr/bin/python

# https://projecteuler.net/problem=10
# Sum of primes below 2.000.000

from itertools import islice
from itertools import count
from math import sqrt

def is_prime(n):
    if n < 2 or n % 2 == 0: return False
    if n == 2 or n == 3: return True
    return all(n%i for i in islice(count(3,2), int(sqrt(n)-1)))

limit = 2000000

# Using the sieve of Erastothenes
sieve_bound = (limit - 1) / 2
sieve = [False] * sieve_bound
# 1 is not a prime number
sieve[0] = True
cross_limit = (int(sqrt(limit)) -1) / 2
for i in xrange(1, cross_limit):
    if sieve[i] == False:
        for j in xrange(2*i*(i+1), sieve_bound, 2*i+1):
            sieve[j] = True

sumation = 2
for i in xrange(0, sieve_bound):
    if sieve[i] == False:
        sumation += (2*i + 1)

print sumation
