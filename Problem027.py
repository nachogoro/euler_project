#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=27
#
# PROBLEM CONTENT:
# Euler discovered the remarkable quadratic formula:
#
# $n^2 + n + 41$
#
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 =
# 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 +
# 41 is clearly divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values 0 <= n <= 79. The product of the
# coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
# n^2 + a*n + b, where |a| < 1000 and |b| <= 1000
#
# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for consecutive values
# of n, starting with n = 0.
#
# EXPLANATION:
# From n = 0, we get that b needs to be a prime
# From n = 1, we get that (a + b + 1) needs to be a prime. Since 2 is the only
# even prime number, if b is 2 then a needs to be even. If b isn't 2, then
# a needs to be odd.

import time
from primes import is_prime, sieve_of_eratosthenes

def prime_run(a, b):
    r = 0
    n = 0
    while True:
        if is_prime(n*n + a*n + b):
            r = r + 1
            n = n + 1
        else:
            return r
def main():
    max_run = 0
    product = 0
    b_set = sieve_of_eratosthenes(1000)

    # With b = 2
    for a in range(-998, 998, 2):
        this_run = prime_run(a, 2)
        if this_run > max_run:
            max_run = this_run
            product = a*2

    # With b != 2
    for a in range(-999, 999, 2):
        for b in b_set[1:]:
            this_run = prime_run(a, b)
            if this_run > max_run:
                max_run = this_run
                product = a*b

    print(product)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
