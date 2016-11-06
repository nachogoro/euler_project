#!/usr/bin/python

# http://projecteuler.net/problem=1
#
# PROBLEM CONTENT:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

# EXPLANATION:
# Sum of divisible by 3: 3+6+9+ ...+999 = 3*(1+2+3...+333)
# Sum of divisible by 5: 5+10+15+ ...+995 = 3*(1+2+3...+199)
# Sum of divisible by 15: 15*(1+2+3...+66)

import time

target = 1000

def main():
    upperBound = target - 1
    end_of_3_mult = int(upperBound/3)
    end_of_5_mult = int(upperBound/5)
    end_of_15_mult = int(upperBound/15)

    sum_mult_3 = 3*end_of_3_mult*(end_of_3_mult+1)/2
    sum_mult_5 = 5*end_of_5_mult*(end_of_5_mult+1)/2
    sum_mult_15 = 15*end_of_15_mult*(end_of_15_mult+1)/2
    print((sum_mult_3 + sum_mult_5 - sum_mult_15))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = (time.time() - start)
    print(('Solved in %.2f seconds' % elapsed))
