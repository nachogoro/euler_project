#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=57
#
# PROBLEM CONTENT:
# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.
#
# √2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# By expanding this for the first four iterations, we get:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than denominator?

import time
from fractions import Fraction

def main():
    expansions = [Fraction(3, 2)]
    for i in range(1, 10**3):
        denominator = 2 + Fraction(1, 2)

        for j in range(0, i):
            denominator = 2 + 1/denominator

        expansions.append(1 + Fraction(1, denominator))

    print(sum(1 for f in expansions if len(str(f.numerator)) > len(str(f.denominator))))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
