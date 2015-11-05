#!/usr/bin/python

# https://projecteuler.net/problem=1
# Sum of all integers below 1000 which are divisible by 3 and 5
# Improved after explanatory pdf, see for further details

num = 999

lim_3 = int(num / 3)
lim_5 = int(num / 5)
lim_15 = int(num / 15)
sum_div_3 = int(3 * (lim_3*(lim_3+1)) / 2)
sum_div_5 = int(5 * (lim_5*(lim_5+1)) / 2)
sum_div_15 = int(15 * (lim_15*(lim_15+1)) / 2)

result = sum_div_3 + sum_div_5 - sum_div_15
print result

