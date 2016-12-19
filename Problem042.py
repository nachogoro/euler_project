#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=42
#
# PROBLEM CONTENT:
# The nth term of the sequence of triangle numbers is given by tn=½n*(n+1); so
# the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10
# If the word value is a triangle number then we shall call the word a
# triangle word.
#
# Using Problem042.data, a 16K text file containing
# nearly two-thousand common English words, how many are triangle words?

import time

def word_score(w):
    score = 0
    for c in w:
        # 'A' - 1 = 64
        score += (ord(c) - 64)
    return score

def triangle_sequence(limit):
    r = []
    n = 1
    next_elem = 1
    while next_elem <= limit:
        r.append(next_elem)
        n += 1
        next_elem = 0.5*n*(n+1)
    return r

def main():
    with open('Problem042.data') as f:
        words = f.read().splitlines()

    scores = [word_score(w) for w in words]
    max_score = max(s for s in scores)

    # Compute the sequence until it covers up to the largest score
    seq = triangle_sequence(max_score)

    print(sum(1 for i in scores if i in seq))


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
