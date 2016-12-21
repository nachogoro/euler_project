#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=58
#
# PROBLEM CONTENT:
# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.
#
#  37 36 35 34 33 32 31
#  38 17 16 15 14 13 30
#  39 18  5  4  3 12 29
#  40 19  6  1  2 11 28
#  41 20  7  8  9 10 27
#  42 21 22 23 24 25 26
#  43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square
# spiral with side length 9 will be formed. If this process is continued, what
# is the side length of the square spiral for which the ratio of primes along
# both diagonals first falls below 10%?

# EXPLANATION:
# The n-th square's diagonal will be 4 numbers, separated 2*(n-1) units, and
# starting from the highest number of the n-1 layer + 2*(n-1)
#
# The n-th square has a dimension of (2*n - 1)

import time
from fractions import Fraction
from primes import is_prime

TARGET = 0.1

def diag_elements_n_square(prev_largest, n):
    return [prev_largest + i*(2*n-2) for i in range(1 ,5)]

def main():
    elements = [1]
    prev_largest = 1
    primes_in_elements = 0
    n = 1

    while True:
        n += 1
        new_elements = diag_elements_n_square(prev_largest, n)
        elements += new_elements
        primes_in_elements += sum(1 for e in new_elements if is_prime(e))
        prev_largest = max(new_elements)
        proportion = primes_in_elements/len(elements)

        if proportion < TARGET:
            print(2*n - 1)
            return


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
