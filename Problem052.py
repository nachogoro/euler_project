#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=52
#
# PROBLEM CONTENT:
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x and 6x,
# contain the same digits.

import time

def fulfils_condition(n):
    ordered_n_str = sorted(str(n))
    return (ordered_n_str == sorted(str(2*n))
            and ordered_n_str == sorted(str(3*n))
            and ordered_n_str == sorted(str(4*n))
            and ordered_n_str == sorted(str(5*n))
            and ordered_n_str == sorted(str(6*n)))

def main():
    n = 0
    while True:
        n += 1
        if fulfils_condition(n):
            print(n)
            return

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
