#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=26
#
# PROBLEM CONTENT:
# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.

# EXPLANATION:
# When dividing two numbersby hand, we use the remainder of the division to
# compute the following digits. For example, taking d=13:
# 1 / 13 = 0        1 % 13 = 1          Partial result = 0
# We would now multiply the remainder by 10 and do it again:
# 10 / 13 = 0       10 % 13 = 10        Partial result = 0.0
# And again:
# 100 / 13 = 7      100 % 13 = 9        Partial result = 0.07
# 90 / 13 = 6       90 % 13 = 12        Partial result = 0.076
# 120 / 13 = 9      120 % 13 = 6        Partial result = 0.0769
# ...
# The moment we get a remainder that we have gotten before, we start the
# recurring cycle. If we get 0 as the remainder, there is no recurring cycle.
#
# To save iterations, we can see that the recurring cycle will stop as soon as
# we get the same remainder twice, and the remainder can only be [1, d-1]. By
# the pidgeonhole theorem, the recurring cycle will be smaller than d. We start
# from the largest d we want to consider, and as soon as our recurring cycle
# becomes larger than the current d we can stop.

import time

def recurring_cycle(d):
    remainders = []
    r = (1 % d)
    while r not in remainders and r != 0:
        remainders.append(r)
        r = (r*10 % d)

    if r == 0:
        return 0

    # r is in remainders, the recurring cycle will be the numbers between the
    # remainder in the list and the end of the list
    return len(remainders) - remainders.index(r)


def main():
    max_cycle = 0
    d = None
    for i in range(1000, 1, -1):
        rec = recurring_cycle(i)
        if rec >= max_cycle:
            max_cycle = rec
            d = i
        elif max_cycle > i:
            break
    print('d: {}, recurring cycle length: {})'.format(d, max_cycle))

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
