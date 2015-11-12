#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=21
#
# PROBLEM CONTENT:
# Let d(n) be defined as the sum of proper divisors of n.
#
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time
from math import sqrt

limit = 10000

def sum_of_proper_divisors(n):
    divisors = 1
    squareRoot = int(sqrt(n))
    for i in xrange(2, squareRoot+1):
        if n%i == 0:
            divisors += i + n/i

    # Correction for perfect square numbers
    if squareRoot**2 == n:
        divisors -= squareRoot
    return divisors

def main():
    amicables = 0
    # We start at 220, the smallest amicable number.
    # When we find a pair, we sum it. No need to check limit-1 (it will have
    # appeared as the amicable pair of a lower number)
    for i in xrange(220, limit-1):
        sumOfDivisors = sum_of_proper_divisors(i)
        if sumOfDivisors > i and sum_of_proper_divisors(sumOfDivisors) == i:
            amicables += i + sumOfDivisors
    print amicables

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
