#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=48
#
# PROBLEM CONTENT:
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

import time

def main():
    result = 0
    for i in range(1, 1001):
        result += i**i

    print(str(result)[-10:])

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
