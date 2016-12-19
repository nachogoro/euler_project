#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=46
#
# PROBLEM CONTENT:
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?
#

# EXPLANATION:

import time
from math import sqrt
from primes import is_prime

def is_perfect_square(n):
    return sqrt(n).is_integer()

def is_decomposable(n):
    for i in range(2, n):
        if is_prime(i) and is_perfect_square(int((n - i)/2)):
            return True

    return False

def main():
    n = 1
    while True:
        n += 2
        if not is_prime(n) and not is_decomposable(n):
            print(n)
            break


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
