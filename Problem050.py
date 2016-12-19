#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=50
#
# PROBLEM CONTENT:
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?
#
#
# EXPLANATION:
# We generate a list with the i-th element being the sum of the first i primes.
# We can use this to compute the sum of all consecutive primes between two
# other primes pi and pj as: cummulative_sum(pj) - cummulative_sum(p(i-1)).
#
# We iterate over this list in two directions: the outer loop going up and the
# inner loop going down from the outer loop variable. We look for the
# difference between these two loops to be prime. If the difference between
# cumulative_sum[i] and cumulative_sum[j] is a prime number, that is a prime
# number which is the sum of i-j consecutive primes.
#
# The inner loop does not go down exactly from the outer loop variable. If we
# have already found an n-consecutive-prime-long sum, i and j need to be
# separated at least (n+1) so that it is of interest for us.

import time
from primes import sieve_of_eratosthenes, is_prime

def main():
    LIMIT = 10**6

    primes = sieve_of_eratosthenes(LIMIT)
    cumulative_sums = [2 for i in primes]

    for i in range(1, len(cumulative_sums)):
        cumulative_sums[i] = primes[i] + cumulative_sums[i-1]

    result = 0
    number_of_primes = 0

    for i in range(0, len(cumulative_sums)):
        for j in range(i - (number_of_primes + 1), -1, -1):
            sum_consecutive_primes = cumulative_sums[i] - cumulative_sums[j]

            # sum_consecutive_primes increases as the inner loop advances. If
            # the difference is already too large, we can break the loop, since
            # it will only grow larger
            if sum_consecutive_primes > LIMIT:
                break

            if is_prime(sum_consecutive_primes):
                number_of_primes = i - j
                result = sum_consecutive_primes

    print(result)
    return

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
