#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=23
#
# PROBLEM CONTENT:
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

import time
from math import sqrt

limit = 28123
abundant_numbers = []

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
    # Find all abundant numbers below 28123
    for i in xrange(12, limit+1):
        if sum_of_proper_divisors(i) > i:
            abundant_numbers.append(i)

    sumOfAbundants = set()

    # Find all the numbers below 28123 which can be expressed as the sum of two
    # abundant numbers.
    # We use a set because it does not allow duplicate objects
    for i, abundant in enumerate(abundant_numbers):
        j = i
        thisSum = abundant + abundant_numbers[j]
        while thisSum <= limit:
            sumOfAbundants.add(thisSum)
            j += 1
            thisSum = abundant + abundant_numbers[j]

    # Sum all the numbers below 28123 which can be expressed as the sum of two
    # abundant numbers
    allSummed = sum(sumOfAbundants)

    # The result is the sum of all numbers from 1 to 28123 minus the sum of all
    # numbers which can be expressed as the sum of two abundant numbers
    print (limit*(limit+1)/2) - allSummed


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
