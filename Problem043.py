#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=43
#
# PROBLEM CONTENT:
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:
#
# d2d3d4  = 406 is divisible by 2
# d3d4d5  = 063 is divisible by 3
# d4d5d6  = 635 is divisible by 5
# d5d6d7  = 357 is divisible by 7
# d6d7d8  = 572 is divisible by 11
# d7d8d9  = 728 is divisible by 13
# d8d9d10 = 289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

import time
from itertools import permutations

def number_from_tuple(tup):
    result = 0
    for c in tup:
        result = result*10 + c
    return result

def is_rather_interesting(n):
    str_rep = str(n)

    return (int(str_rep[1:4]) % 2 == 0
            and int(str_rep[2:5]) % 3 == 0
            and int(str_rep[3:6]) % 5 == 0
            and int(str_rep[4:7]) % 7 == 0
            and int(str_rep[5:8]) % 11 == 0
            and int(str_rep[6:9]) % 13 == 0
            and int(str_rep[7:10]) % 17 == 0)

def main():
    # Get all 0-9 pandigital numbers
    all_pandigital = [number_from_tuple(i) for i in permutations(range(9, -1, -1))]

    # Add together those which have the "rather interesting property"
    print(sum(n for n in all_pandigital if is_rather_interesting(n)))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
