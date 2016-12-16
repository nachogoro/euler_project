#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=34
#
# PROBLEM CONTENT:
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# EXPLANATION:
# Upper bound found because the number grows faster that the sum of the
# factorial of its digits once the number is big enough. A new digit adds at
# most 9! = 362880. Once the number is larger than 7*9! = 2540160, a new digit
# adds more to the number itself (multiplies it by 10) than to the sum of the
# factorial.

import time

from math import factorial

UPPER_BOUND = 2540160

def is_curious(num):
    num_str = str(num)
    result = 0
    for d in num_str:
        result += factorial(int(d))
        if (result > num):
            return False

    return result == num

def main():
    result = 0
    for i in range(10, UPPER_BOUND):
        if is_curious(i):
            result += i

    print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
