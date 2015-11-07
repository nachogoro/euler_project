#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=9
#
# PROBLEM CONTENT:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
#
# Find the product a*b*c.

# EXPLANATION:
# Take into account that a < b < c, so a can be at most 1000/3 and b (1000-a)/2

import time

limit = 1000

def main():
    for a in xrange(1, int(limit/3)+1):
        for b in xrange(a+1, int((limit-a)/2)+1):
            c = limit - a - b
            if a*a + b*b == c*c:
                print a*b*c

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
