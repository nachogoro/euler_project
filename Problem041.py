#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=41
#
# PROBLEM CONTENT:
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
#
# What is the largest n-digit pandigital prime that exists?
#

# EXPLANATION:
# itertools.permutations returns all the possible permutations of an iterable
# (in order if the iterable was ordered). I first check (in descending order)
# all the permutations of 9 digits for primality, then all the permutations of
# 8 digits, etc.

import time

from itertools import permutations
from primes import is_prime


def number_from_tuple(tup):
    result = 0
    for c in tup:
        result = result*10 + c
    return result

def main():
    nums = [i for i in range(9, 0, -1)]

    for i in range(0, len(nums)):
        ordered_permutations = list(permutations(nums[i:]))

        for p in ordered_permutations:
            candidate = number_from_tuple(p)
            if is_prime(candidate):
                print(candidate)
                return

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
