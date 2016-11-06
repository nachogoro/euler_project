#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=22
#
# PROBLEM CONTENT:
# Using the attached 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import time

def main():
    names_list = None
    with open('Problem022.data') as f:
        # Do not use readlines() to get rid of the '\n'
        names_list = f.read().splitlines()
    names_list.sort()

    result = 0

    for index, name in enumerate(names_list):
        score = 0
        for letter in name:
            score += (ord(letter) - ord('A') + 1)
        result += (index+1)*score

    print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
