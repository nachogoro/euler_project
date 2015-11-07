#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=6
#
# PROBLEM CONTENT:
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


import time

limit = 100

def main():
    square_sum = limit*(limit+1)/2
    square_sum *= square_sum
    sum_of_squares = (2*limit+1)*(limit+1)*limit/6
    print (square_sum - sum_of_squares)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
