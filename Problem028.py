#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=28
#
# PROBLEM CONTENT:
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

# EXPLANATION:
# The n-th square's diagonal will be 4 numbers, separated 2*(n-1) units, and
# starting from the highest number of the n-1 layer + 2*(n-1)
#
# The n-th square has a dimension of (2*n - 1)
# The 501th square has 1001 elements per side

import time

def diag_sum_n_square(prev_largest, n):
    result = 0
    for i in range(1, 5):
        result = result + prev_largest + i*(2*n - 2)
    return result

def main():
    diag_sum = 1
    prev_largest = 1
    for n in range(2, 502):
        diag_sum = diag_sum + diag_sum_n_square(prev_largest, n)
        prev_largest = prev_largest + 4*(2*n - 2)
    print(diag_sum)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
