#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=36
#
# PROBLEM CONTENT:
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

import time

def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def binary_representation(n):
    return bin(n)[2:]

def main():
    result = 0
    # Since there can't be any leading zeroes, even numbers would never be
    # palyndromic in binary
    for n in range(1, 10**6 + 1, 2):
        if is_palindrome(n) and is_palindrome(binary_representation(n)):
            result += n

    print(result)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
