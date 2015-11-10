#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=20
#
# PROBLEM CONTENT:
# n! means n x (n-1) x ... x 3 x 2 x 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the
# digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# EXPLANATION:

import time
from math import factorial

def main():
    value = str(factorial(100))
    print sum(int(x) for x in value)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
