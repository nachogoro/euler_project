#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=47
#
# PROBLEM CONTENT:
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
#
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
#
# 645 = 3 × 5 × 43
#
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors
# each. What is the first of these numbers?

import time
from primes import prime_factors, sieve_of_eratosthenes

def main():
    current_sieve_limit = 100000
    sieve = sieve_of_eratosthenes(current_sieve_limit)

    n = 2*3*4*5 - 1
    while True:
        n += 1

        # Re-compute the sieve
        if n > current_sieve_limit:
            current_sieve_limit *= 2
            sieve = sieve_of_eratosthenes(current_sieve_limit)

        if (len(prime_factors(n, sieve)) == 4
                and len(prime_factors(n+1, sieve)) == 4
                and len(prime_factors(n+2, sieve)) == 4
                and len(prime_factors(n+3, sieve)) == 4):
            print(n)
            break

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
