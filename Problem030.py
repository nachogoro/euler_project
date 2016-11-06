#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=30
#
# PROBLEM CONTENT:
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.
#

# EXPLANATION:
# They need to be shorter than 7 digits

import time

def main():
    total_result = 0
    for i in range(2, 1000000):
        str_rep = str(i)
        this_num_sum = 0
        for c in str_rep:
            this_num_sum = this_num_sum + int(c)**5
        if this_num_sum == i:
            total_result = total_result + i
    print(total_result)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
