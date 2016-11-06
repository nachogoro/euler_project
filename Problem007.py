#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=7
#
# PROBLEM CONTENT:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?


from primes import is_prime
import time

target = 10001

def main():
    primes_found = 1
    last_candidate = 1

    while primes_found < target:
        last_candidate += 2
        if is_prime(last_candidate):
            primes_found += 1

    print(last_candidate)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
