#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=15
#
# PROBLEM CONTENT:
# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#
# EXPLANATION:
# The number of paths from a point to the bottom-right corner is the sum of the
# number of paths from the point on its right to the bottom-right corner + the
# number of paths from the point below it to the bottom-right corner. Points at
# the border of the grid only have one possible path to the bottom-right
# corner: always right or always down. Setting the boundary conditions we can
# work recursively from the almost-bottom-right corner to the top-right corner.
#
# For a 2x2 grid (note: there n+1 nodes):
# 0--0--1       0--0--1       0--3--1       6--3--1
# 0--0--1  ---> 0--2--1  ---> 3--2--1  ---> 3--2--1 ---> Answer: 6
# 1--1--1       1--1--1       1--1--1       1--1--1
#
# A square matrix like this one can be simplified further by only computing the
# terms of one of the top diagonal part, since it is simmetric. I have decided
# to use a more general method.

import time

horDim = 20
verDim = 20


def initialise_nodes_grid(nodesGrid):
    defaultRow = [0 for i in range(0,horDim+1)]
    defaultRow[horDim] = 1
    for i in range(0, verDim):
        nodesGrid.append(defaultRow)
    nodesGrid.append([1 for i in range(0, horDim+1)])

def main():
    # Matrix representing the number of paths from a node to the bottom-right
    # corner
    nodesGrid = []
    initialise_nodes_grid(nodesGrid)
    for i in range(verDim-1, -1, -1):
        for j in range(horDim-1, -1, -1):
            nodesGrid[i][j] = nodesGrid[i+1][j] + nodesGrid[i][j+1]
    print(nodesGrid[0][0])

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
