#!/usr/bin/python

# https://projecteuler.net/problem=7
# 10001st prime number

from itertools import islice
from itertools import count
from math import sqrt

def is_prime(n):
    if n < 2 or n % 2 == 0: return False
    if n == 2 or n == 3: return True
    return all(n%i for i in islice(count(3,2), int(sqrt(n)-1)))

primes_found=1
last_candidate=3

while True:
    if is_prime(last_candidate):
        primes_found = primes_found+1
        if primes_found == 10001:
            print last_candidate
            break
    last_candidate = last_candidate + 1

