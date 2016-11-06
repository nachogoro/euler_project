#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=25
#
# PROBLEM CONTENT:
# The 12th term of the Fibonacci sequence is the first term to contain three
# digits.
#
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?
#

# EXPLANATION:
# Iteratively find the number with a binary search.

import time
from fibonacci import fibonacci_generator

def main():
    index = 1
    for term in fibonacci_generator():
        if len(str(term)) >= 1000:
            print(index)
            break
        index += 1

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
