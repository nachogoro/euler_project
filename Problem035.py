#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=35
#
# PROBLEM CONTENT:
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import time
from primes import sieve_of_eratosthenes, is_prime

def get_rotations(n):
    n_rotations = len(str(n))
    rotations = [n for i in range(0, n_rotations)]


    for i in range(1, n_rotations):
        # Take last digit and append it to the beginning
        rotations[i] = int(rotations[i-1]/10) + (rotations[i-1]%10)*10**(n_rotations-1)

    return rotations

def main():
    result = 0
    for i in sieve_of_eratosthenes(10**6):
        rotations = get_rotations(i)
        if len(list(filter(lambda x : is_prime(x), rotations))) == len(rotations):
            result+=1

    print(result)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
