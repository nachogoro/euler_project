#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=56
#
# PROBLEM CONTENT:
# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a^b, where a,b < 100, what is the
# maximum digital sum?

import time

def main():
    print(max([sum(int(d) for d in str(a**b)) for a in range(0,100) for b in range(0,100)]))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
