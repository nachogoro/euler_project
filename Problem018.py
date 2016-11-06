#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=18
#
# PROBLEM CONTENT:
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                75
#               95 64
#              17 47 82
#             18 35 87 10
#            20 04 82 47 65
#           19 01 23 75 03 34
#          88 02 77 73 07 63 67
#         99 65 04 28 06 16 70 92
#        41 41 26 56 83 40 80 70 33
#       41 48 72 33 47 32 37 16 94 29
#      53 71 44 65 25 43 91 52 97 51 14
#     70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# As there are only 16384 routes, it is possible to solve this problem by
# trying every route. However, Problem 67 is the same challenge with a triangle
# containing one-hundred rows; it cannot be solved by brute force, and requires
# a clever method! ;o)

# EXPLANATION:
# Work from the bottom up, converting each node in the maximum 'score' one
# could get if decided to pick that node.
# From a row of N elements, generate a row of N-1 elements by choosing the
# greatest of two adjacent numbers. The nth entry of this new row is the value
# of the highest scoring node the nth node from the row on top could pick. We
# can then sum the new row to the one of top and iteratively repeat the process
# until we get to the top.

import time

def initialise():
    with open('Problem018.data') as triangleFile:
        lines = triangleFile.readlines()
    triangle = []
    for line in lines:
        tmpList = line.split()
        # Parse str to int
        triangle.append(list(map(int, tmpList)))

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
            for i in range(0, len(row)-1):
                newRow.append(max(row[i], row[i+1]))

        # Sum it to the previous row and repeat the process
        if (index != 0):
            for i in range(0, len(newRow)):
                triangle[index-1][i] += newRow[i]

    print(triangle[0])


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
