#!/usr/bin/python

# https://projecteuler.net/problem=9
# Pythagorean triplet for which a + b +c = 1000

sum = 1000

for a in range(1,int(sum/3)+1):
    for b in range(a+1,int((sum-a)/2)+1):
        c = sum - a - b
        if a*a + b*b == c*c:
            print "a=%d b=%d c=%d" % (a,b,c)
            print a*b*c
