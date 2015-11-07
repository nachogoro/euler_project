#!/usr/bin/python

# http://projecteuler.net/problem=3
#
# PROBLEM CONTENT:
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

import time
from primes import sieve_of_eratosthenes
from primes import prime_factors

num = 600851475143

def main():
    print prime_factors(num)[-1]

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
