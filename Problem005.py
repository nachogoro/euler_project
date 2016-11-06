#!/usr/bin/python

# http://projecteuler.net/problem=5
#
# PROBLEM CONTENT:
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#

# EXPLANATION:
# We want to compute the lcm of numbers 1-20. The lcm of a set of numbers can 
# be computed recursively: lcm(a, b, c) = lcm(lcm(a,b), c)
# lcm(a,b) = a*b/gcd(a,b)

import time

def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

num = 20

def main():
    result = 2
    for i in range(3, num+1):
        result = lcm(i, result)
    print(result)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
