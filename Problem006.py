#!/usr/bin/python

# https://projecteuler.net/problem=6
# Difference between the sum of the squares of the first 100 natural numbers and the
# square of the sum

n_elem = 100

sum = n_elem*(n_elem+1)/2

sum_of_squares = (2*n_elem+1)*(n_elem+1)*n_elem/6

print (sum*sum - sum_of_squares)

