#!/usr/bin/python

# https://projecteuler.net/problem=5
# Smallest positive number that is evenly divisible by all numbers 1-20

def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

result = lcm(1,2)
for i in range(3,21):
    result = lcm(i, result)

print result
