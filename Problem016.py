#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=16
#
# PROBLEM CONTENT:
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000 ?
#

import time

def main():
    twoToThe1000 = str(2**1000)
    sum = 0
    for i in twoToThe1000:
        sum += int(i)
    print sum

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
