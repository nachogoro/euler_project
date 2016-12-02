#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=31
#
# PROBLEM CONTENT:
# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
# 1p, 2p, 5p 10p, 20p, 50p, £1 (100p) and £2 (200p)
#
# It is possible to make £2 in the following way:
# 1x£1 + 1x50p + 2x20p + 1x5p + 1x2p +3x1p
#
# How many different ways can £2 be made using any number of coins?

# EXPLANATION:
# We will build an array in which the n-th element expresses the number of ways
# n pence can be decomposed.
#
# We build the array iteratively from the fact that there is one way to
# decompose 0p (giving no coins). We then see how many ways we can give each
# amount using only 1p coins. Once we've done that, we add the possibility of
# using 2p coins. For that, we use the previously computed information: we know
# there are n ways of giving 2p using 1p coin. If we used one 2p coin, we end
# up needing to give 0p (there is one way to give it), so the ways of giving 2p
# using 2p coins or smaller is the number of ways of giving it using 1p + 1.
# For 3p, if we gave one 2p coin we would need to give 1p change, which we have
# already computed how many ways we can give it using 2p coins or smaller, so
# add it to the current number of ways using just 1p coins.
#
# Graphically, using only 1p, 2p and 5p coins, let's decompose until 5p. We
# first build the number of ways to decompose using only 1p coins:
#
# Full table using 1p:
# +----------+---+---+---+---+---+---+
# |  Amount  | 0 | 1 | 2 | 3 | 4 | 5 |
# +----------+---+---+---+---+---+---+
# |   Ways   | 1 | 1 | 1 | 1 | 1 | 1 |
# +----------+---+---+---+---+---+---+
#
# Now, using 2p coins or smaller we build on the previous table. 0p and 1p are
# left untouched. For 2p we can give one 2p coin, leaving us with 0p remainder.
# We add the current value for 2 (1) and the current value for 0 (1)
#
# Partial table using 2p or smaller (computed until 2p):
# +----------+---+---+---+---+---+---+
# |  Amount  | 0 | 1 | 2 | 3 | 4 | 5 |
# +----------+---+---+---+---+---+---+
# |   Ways   | 1 | 1 | 2 | 1 | 1 | 1 |
# +----------+---+---+---+---+---+---+
#
# For 3p we can give one 2p coin and we are left with 1p remainder. We add the
# current value for 3p (1) with the current value for 1p (1):
#
# Partial table using 2p or smaller (computed until 3p):
# +----------+---+---+---+---+---+---+
# |  Amount  | 0 | 1 | 2 | 3 | 4 | 5 |
# +----------+---+---+---+---+---+---+
# |   Ways   | 1 | 1 | 2 | 2 | 1 | 1 |
# +----------+---+---+---+---+---+---+
#
# For 4p we can give one 2p coin and we are left with 2p remainder. We add the
# current value for 4p (1) with the current value for 2p (2):
#
# Partial table using 2p or smaller (computed until 4p):
# +----------+---+---+---+---+---+---+
# |  Amount  | 0 | 1 | 2 | 3 | 4 | 5 |
# +----------+---+---+---+---+---+---+
# |   Ways   | 1 | 1 | 2 | 2 | 3 | 1 |
# +----------+---+---+---+---+---+---+
#
# For 5p we can give one 2p coin and we are left with 3p remainder. We add the
# current value for 5p (1) with the current value for 3p (2):
#
# Full table using 2p or smaller:
# +----------+---+---+---+---+---+---+
# |  Amount  | 0 | 1 | 2 | 3 | 4 | 5 |
# +----------+---+---+---+---+---+---+
# |   Ways   | 1 | 1 | 2 | 2 | 3 | 3 |
# +----------+---+---+---+---+---+---+
#
# We now switch to use 5p coins or smaller. All the amounts smaller than 5p are left untouched.
# For 5p we can give one 5p coin and we are left with 0p remainder. We add the
# current value for 5p (3) with the current value for 0p (1):
#
# Full table using 2p or smaller:
# +----------+---+---+---+---+---+---+
# |  Amount  | 0 | 1 | 2 | 3 | 4 | 5 |
# +----------+---+---+---+---+---+---+
# |   Ways   | 1 | 1 | 2 | 2 | 3 | 4 |
# +----------+---+---+---+---+---+---+

import time

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]


def main():
    # £2 in pence
    amount = 200

    # Initialise array to zero
    ways = [0 for x in range(amount + 1)]

    # There is one way of giving 0p change: no coins
    ways[0] = 1

    for coin in coin_values:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]

    print(ways[amount])



if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
