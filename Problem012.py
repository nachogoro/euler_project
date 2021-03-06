#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=12
#
# PROBLEM CONTENT:
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?


# EXPLANATION:
# The number of divisors of a number N = p1^a1 * p2^a2 * p3^a3...,where p_i are
# the prime factors of N and a_i the correspondent power, is:
# D(N) = (a1+1)*(a2+1)*(a3+1)...
#
# A triangular number is of the form N = n*(n+1)/2
# Since n and (n+1) are necessarily co-prime (they do not share prime factors, 
# so the have no common divisor). The total number of divisors for N can then be
# obtained as D(N) = D(n/2) * D(n+1) if n is even or as D(N) = D(n) * D((n+1)/2) 
# if n is odd
#
# Also, in each iteration, our num_divisors(n+1) is the num_divisors(n) for the 
# next iteration

import time

def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n

def main():
    index = find_triangular_index(500)
    triangle = (index * (index + 1)) / 2
    print(triangle)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
