#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=49
#
# PROBLEM CONTENT:
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit increasing
# sequence.
#
# What 12-digit number do you form by concatenating the three terms in this
# sequence?
#
#
# EXPLANATION:
# The question is to find another tuple of three numbers whose values are
# separated a fixed distance (not necessarily 3330) which are permutations of
# each other and are primes.
# We compute all the 4-digit prime numbers, and iterate over it with two primes
# (i and j). We find a number which is equally separated from j than i (k) and
# see if the values are the desired tuple.

import time

from itertools import permutations
from functools import reduce
from primes import is_prime, sieve_of_eratosthenes

def is_permutation(a, b):
    b = str(b)
    for c in str(a):
        b = b.replace(c, '', 1)
    return len(b) == 0

def main():
    sieve = sieve_of_eratosthenes(10**4)
    beginning = next(i for i,val in enumerate(sieve) if val >= 1001)
    sieve = sieve[beginning:]

    for indexi,i in enumerate(sieve):
        for j in sieve[indexi+1:]:
            k = j + (j - i)
            if (is_permutation(i, j)
                    and is_prime(k)
                    and is_permutation(i, k)
                    and (i != 1487 and j != 4817 and k != 8147)):
                print('{}{}{}'.format(i, j, k))
                return



if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
