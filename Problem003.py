#!/usr/bin/python

# https://projecteuler.net/problem=3
# Largest prime factor of 600851475143

from math import sqrt

num = 600851475143

last_factor = 1

if num % 2 == 0:
    last_factor = 2
    num = num / 2
    while num % 2 == 0:
        num = num / 2
else:
    last_factor = 1

factor = 3
max_factor = int(sqrt(num))

while num > 1 and factor <= max_factor:
    if num % factor == 0:
        num = num / factor
        last_factor = factor
        while num % factor == 0:
            num = num / factor
        max_factor = sqrt(num)
    factor = factor + 2

if num == 1:
    print last_factor
else:
    print num
