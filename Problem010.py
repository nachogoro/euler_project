#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=10
#
# PROBLEM CONTENT:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#

# EXPLANATION:

import time
from primes import sieve_of_eratosthenes

limit = 2000000

def main():
    print(sum(sieve_of_eratosthenes(limit-1)))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
