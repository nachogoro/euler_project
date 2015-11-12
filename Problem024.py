#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=24
#
# PROBLEM CONTENT:
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

# EXPLANATION:
# With 10 numbers, there are 10! permutations. The first 9! (362,880)
# permutations will start with number 0. Then, the next 9! will start with a 1.
# We then see that the 1,000,000th permutation will start with a 2 (since the
# permutations starting with a 2 will be numbers 725,760 to 1,088,640).
# We can then fix number 2 and see how many permutations to go from the first
# one starting with 2 (725,760) to the desired one (1,000,000), and repeat the
# operation.

import time
from math import factorial
import sys

desiredPermutation = 1e6
numbersToPermute = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    # Ordered list which will store the desired permutation
    desiredSequence = []
    # Number of elements which have not been 'fixed' yet
    numberOfElements = len(numbersToPermute)
    # How many permutation to go from now to the desired one
    targetPermutation = desiredPermutation -1

    while len(desiredSequence) != numberOfElements:
        # Find next number of the sequence
        nextNumberOfSequence = int(targetPermutation / factorial(len(numbersToPermute)-1))
        # Find out how many iterations from this one we need
        targetPermutation = targetPermutation % factorial(len(numbersToPermute)-1)
        desiredSequence.append(numbersToPermute[nextNumberOfSequence])
        numbersToPermute.pop(nextNumberOfSequence)

    for letter in desiredSequence:
        sys.stdout.write(str(letter))
    print

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
