#!/usr/bin/python

# https://projecteuler.net/problem=2
# Sum of the even-valued terms of the Fibonacci sequence

before_last = 1
last = 2

acc_sum = 0

while last < 4000000:
    if last%2 == 0:
        acc_sum += last
    aux = last
    last += before_last
    before_last = aux

print acc_sum
