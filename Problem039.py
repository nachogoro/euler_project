#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=39
#
# PROBLEM CONTENT:
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p=120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

import time
from math import sqrt

PERIMETER_LIMIT = 1000


def main():
    solutions = {}

    for a in range(1, 1000):
        for b in range(1, a):
            c = sqrt(a**2 - b**2)

            if a+b+c > PERIMETER_LIMIT or c < b or not c.is_integer():
                continue

            perimeter = a+b+int(c)
            if perimeter in solutions:
                solutions[perimeter] += 1
            else:
                solutions[perimeter] = 1

    print(max(solutions, key=solutions.get))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
