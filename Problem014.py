#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=14
#
# PROBLEM CONTENT:
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3*n+1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# Once the chain starts the terms are allowed to go above one million.
#

# EXPLANATION:
# We can cache the number of jumps until one for each seed and re-use it.

import time

def next_element(n):
    if n%2:
        return 3*n+1
    else:
        return n/2

limit = int(1e6)

def main():
    # Maps seed to number of jumps until 1
    jumpsUntilOne = {}
    jumpsUntilOne[1] = 0
    longestSequence = 0
    longestSeed = None

    for i in range(2, limit-1):
        nJumps = 1
        currentNumber = i
        while currentNumber != 1:
            currentNumber = next_element(currentNumber)
            nJumps += 1
            if currentNumber < i:
                nJumps += jumpsUntilOne[currentNumber]
                break
        if nJumps > longestSequence:
            longestSequence = nJumps
            longestSeed = i
        jumpsUntilOne[i] = nJumps

    print(longestSeed)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
