#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=51
#
# PROBLEM CONTENT:
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.
#

# EXPLANATION:
# Brute force it. If there are 8 primes in the 10-member family and we are
# interested in the smaller member of the family, the replaced digits need to
# be 0, 1 or 2 (otherwise, the family cannot be formed of 8 members).
# Generate a large list of primes and iterate over it. For each prime we find
# the indices of its 0, 1 and 2 digits. We then combine them to obtain all
# possible families.
#
# Example for n = 112125 (imagining 112125 were prime)
# We generate a dictionary of the indices: {'1':[0,1,3], '2':[2,4]}
# We then combine the elements of each list with the other elements of the list:
# [(0,1), (0,3), (1,3), (0,1,3), (2,4)]
# There will be 5 families which might potentially be composed of primes:
# **2125: [112125, 222125, 332125, 442125, 552125, 662125, 772125, 882125, 992125]
# *12*25: [112125, 212225, 312325, 412425, 512525, 612625, 712725, 812825, 912925]
# 1*2*25: [102025, 112125, 122225, 132325, 142425, 152525, 162625, 172725, 182825, 192925]
# **2*25: [112125, 222225, 332325, 442425, 552525, 662625, 772725, 882825, 992925]
# 11*1*5: [110105, 111115, 112125, 113135, 114145, 115155, 116165, 117175, 118185, 119195]
#
# We would check all the generated families

import time
from primes import is_prime, sieve_of_eratosthenes
from itertools import combinations

# Return the indices of all the 0, 1 and 2 in the string representation of p
def generate_dict(p):
    digit_index = {}

    for c in range(0, 3):
        digit_index[c] = [i for i,v in enumerate(p) if v == str(c)]

    return digit_index

def get_potential_families(p):
    p_str = str(p)
    digit_indices = generate_dict(p_str)
    combination_of_indices = []

    # Generate a list of tuples of all the combinations of the indices of the
    # digits of interest
    for d in digit_indices:
        for c in range(2, len(digit_indices[d]) + 1):
            combination_of_indices += list(combinations(digit_indices[d], c))

    families = [[] for i in combination_of_indices]

    # Generate all the possible families by replacing the digits at the index
    # with 0-9
    for i,tup in enumerate(combination_of_indices):
        modified_p = list(p_str)
        for d in range(0, 10):
            for element in tup:
                modified_p[element] = str(d)

            # We do not count leading zeroes (e.g. 111109 would generate 109,
            # but we do not consider it a valid member of the family)
            modified_p_int = int(''.join(modified_p))
            if len(str(modified_p_int)) == len(p_str):
                families[i].append(modified_p_int)

    return families


def main():
    primes = sieve_of_eratosthenes(10**6)

    for p in primes:
        families = get_potential_families(p)
        for f in families:
            if sum(1 for i in f if is_prime(i)) >= 8:
                print(f[0])
                return

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
