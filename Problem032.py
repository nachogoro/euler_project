#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=32
#
# PROBLEM CONTENT:
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is
# 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# Explanation:
# As soon as the multiplicand is 4 digits, so is the product, so the upper
# limit for multiplicand/multiplier is 9876

import time


def is_pandigital(string):
    removed_duplicates = set(string)
    return (len(removed_duplicates) == 9
            and sorted(removed_duplicates)[0] == '1')


def main():
    result = 0
    products = []

    for multiplicand in range(2, 9876):
        for multiplier in range(multiplicand + 1, 9876):
            product = multiplicand * multiplier
            string = str(product) + str(multiplicand) + str(multiplier)
            if len(string) > 9:
                # No need to keep checking
                break

            if (len(string) == 9
                    and is_pandigital(string)
                    and product not in products):
                result += product
                products.append(product)

    print(result)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
