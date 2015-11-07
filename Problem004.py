#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=4
#
# PROBLEM CONTENT:
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    max_palindrome = 0
    a = 999
    while a >= 100:
        b = 999
        while b >= a:
            if a*b <= max_palindrome:
                break
            if is_palindrome(a*b):
                max_palindrome = a*b
            b -= 1
        a -= 1
    print max_palindrome

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
