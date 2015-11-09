#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=67
#
# PROBLEM CONTENT:
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in the next one-hundred-row
# triangle.
#
# This is a much more difficult version of Problem 18. It is not possible to
# try every route to solve this problem, as there are 2^99 altogether! If you
# could check one trillion routes every second it would take over twenty
# billion years to check them all. There is an efficient algorithm to solve it.


# EXPLANATION:
# See Problem018.py

import time

def initialise():
    with open('Problem067.data') as triangleFile:
        lines = triangleFile.readlines()
    triangle = []
    for line in lines:
        tmpList = line.split()
        # Parse str to int
        triangle.append(map(int, tmpList))

    return triangle

def main():
    triangle = initialise()
    for index, row in reversed(list(enumerate(triangle))):
        # From row of N elements generate a row of N-1 elements by choosing the
        # greatest of two adjacent numbers.
        newRow = []
        if len(row) == 1:
            newRow.append(row[0])
        else:
            for i in xrange(0, len(row)-1):
                newRow.append(max(row[i], row[i+1]))

        # Sum it to the previous row and repeat the process
        if (index != 0):
            for i in xrange(0, len(newRow)):
                triangle[index-1][i] += newRow[i]

    print triangle[0]

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
