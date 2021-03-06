#!/usr/bin/python3
# coding:utf8

# http://projecteuler.net/problem=62
#
# PROBLEM CONTENT:
# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are
# cube.
#
#
# EXPLANATION:
# Iterate over the list of integers, computing their cube. From each cube we
# obtain its lowest permutation (just a arbitrary convention so that we can map
# all permutations of the same number to a single key). We store the
# information in a dictionary in which the permutation is the key and the
# values are the lowest integer which generated a permutation of the key and
# the number of integers which, when cubed, generate a permutation of the key.
# We stop as soon as we find a pemrutation which has been generated by 5
# different cubes.


import time
from collections import namedtuple, Counter


Cube = namedtuple('Cube', ['n', 'perms'])


def main():
    n = 345
    cubes = dict()

    while True:
        n += 1
        smallest_perm = int(''.join(sorted(str(n**3))))
        if smallest_perm not in cubes:
            cubes[smallest_perm] = Cube(n=n, perms=0)

        perms = cubes[smallest_perm].perms

        cubes[smallest_perm] = cubes[smallest_perm]._replace(perms=perms+1)

        if cubes[smallest_perm].perms == 5:
            print(cubes[smallest_perm].n**3)
            break


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
