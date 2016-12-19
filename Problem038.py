#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=38
#
# PROBLEM CONTENT:
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We
# will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product
# of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?
#
# EXPLANATION:
# n needs to be larger than 1, so the number we use as 'seed' needs to be less
# than 5 digits long.
# We are given 918273645 as an example, so we need to beat it. That means our
# 'seed' needs to begin with 9 as well. The 'seed' cannot be 2 digits long,
# since n=3 would generate an 8-digit number and n=4 would generate an 11-digit
# number. It cannot be 3 digits long either for the same reason. It is
# therefore a 4-digit number starting with 9, with n=2 (n=3 would already be
# too large)

import time

def is_pandigital(n):
    string = str(n)
    if len(string) != 9:
        return False

    removed_duplicates = set(string)
    return (len(removed_duplicates) == 9
            and sorted(removed_duplicates)[0] == '1')

def main():
    max_pandigital = 918273645

    for i in range(9123, 9876):
        concat = int(str(i) + str(2*i))
        if concat > max_pandigital and is_pandigital(concat):
            max_pandigital = concat

    print(max_pandigital)



if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
