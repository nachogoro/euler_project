#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=40
#
# PROBLEM CONTENT:
# An irrational decimal fraction is created by concatenating the positive
# integers:
# 0.12345678910112131415161718192021...
#              ^
# It can be seen that the 12 digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the
# following expression:
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
# EXPLANATION:
# Brute-forced because it's easier to code than the elegant answer

import time

def main():
    r = ''
    i = 1
    while len(r) < 10**6:
        r += str(i)
        i += 1

    print(int(r[0]) * int(r[9]) * int(r[99]) * int(r[999]) * int(r[9999]) * int(r[99999]) * int(r[999999]))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
