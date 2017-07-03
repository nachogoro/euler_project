#!/usr/bin/python3
# coding:utf8

# http://projecteuler.net/problem=63
#
# PROBLEM CONTENT:
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
#
#
# EXPLANATION:
# We are looking for numbers such that 10^(n-1) <= x^n < 10^n.
# It is clear that x <= 9 from the second part of inequality.
# To obtain x's lower bound we take logs, isolate x and take powers again, to
# obtain x >= 10^((n-1)/n).
#
# As n increases, x tends to 10, which means that at some point the lower bound
# will be larger than the upper bound, and we can stop. So for each n we obtain
# the number of available x, which is 10 - lower_bound; and we stop as soon as
# x is greater than 9.

import time
import math


def main():
    result = 0
    lower = 0
    n = 1

    while lower < 10:
        lower = math.ceil(math.pow(10, (n-1)/n))
        result += 10 - lower
        n += 1
    print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
