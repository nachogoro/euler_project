#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=60
#
# PROBLEM CONTENT:
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
# primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
# these four primes, 792, represents the lowest sum for a set of four primes
# with this property.
#
# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

# EXPLANATION:
# Brute force. We first assume that all the primes are below 27000 (we know
# this a posteriori). We then compute all primes below that limit and attempt
# to combine them. We have a dictionary which maps p to all the primes larger
# than p which concatenate with p to form other primes (to prevent rerunning
# the same computation several times)

import time
from primes import sieve_of_eratosthenes, is_prime

all_primes = sieve_of_eratosthenes(27000)
computed_concats = {2:[]}

def compute_concats(p):
    computed_concats[p] = []
    begin = all_primes.index(p)

    for i in range(begin+1, len(all_primes)):
        prime = all_primes[i]
        if is_prime(int(str(p)+str(prime))) and is_prime(int(str(prime)+str(p))):
            computed_concats[p].append(prime)


def can_be_added(group, prime_to_add):
    for p in group:
        if prime_to_add not in computed_concats[p]:
            return False
    return True


def main():
    # High value
    result = 10**6

    for i1 in range(0, len(all_primes)):
        p1 = all_primes[i1]
        group = [p1]

        if p1 not in computed_concats: compute_concats(p1)

        if sum(group) > result - 4*p1:
            group.pop()
            break

        for i2 in range(i1+1, len(all_primes)):
            p2 = all_primes[i2]

            if can_be_added(group, p2):
                group.append(p2)
                if p2 not in computed_concats: compute_concats(p2)

                if sum(group) > result - 3*p2:
                    group.pop()
                    break

                for i3 in range(i2+1, len(all_primes)):
                    p3 = all_primes[i3]
                    if can_be_added(group, p3):
                        group.append(p3)
                        if p3 not in computed_concats: compute_concats(p3)

                        if sum(group) > result - 2*p3:
                            group.pop()
                            break

                        for i4 in range(i3+1, len(all_primes)):
                            p4 = all_primes[i4]
                            if can_be_added(group, p4):
                                group.append(p4)
                                if p4 not in computed_concats: compute_concats(p4)

                                if sum(group) > result - p4:
                                    group.pop()
                                    break

                                for i5 in range(i4+1, len(all_primes)):
                                    p5 = all_primes[i5]
                                    if can_be_added(group, p5):
                                        group.append(p5)
                                        if sum(group) < result:
                                            result = sum(group)
                                        group.pop()
                                        break
                                group.pop()
                        group.pop()
                group.pop()

    print(result)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
