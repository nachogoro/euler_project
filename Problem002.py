#!/usr/bin/python

# http://projecteuler.net/problem=2
#
# PROBLEM CONTENT:
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
#

import time
from fibonacci import fibonacci_generator

limit = 4e6

def main():
    result = 0
    for i in fibonacci_generator():
        if i >= limit:
            break
        if i%2 == 0:
            result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
