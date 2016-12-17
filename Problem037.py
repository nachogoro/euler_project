#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=37
#
# PROBLEM CONTENT:
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
# left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left
# to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time
from primes import sieve_of_eratosthenes, is_prime

def is_prime_left(n):
    for i in range(len(str(n)), 0, -1):
        if not is_prime(n % 10**i):
            return False
    return True

def is_prime_right(n):
    for i in range(0, len(str(n))):
        if not is_prime(int(n/10**i)):
            return False
    return True


def main():
    result = 0
    found = 0
    i = 10
    while found < 11:
        i += 1
        if is_prime_right(i) and is_prime_left(i):
            found += 1
            result += i

    print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
