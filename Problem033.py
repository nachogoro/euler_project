#!/usr/bin/python3
#coding:utf8

# http://projecteuler.net/problem=33
#
# PROBLEM CONTENT:
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and
# denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

import time
from fractions import Fraction

def main():
    result_fraction = Fraction(1, 1)

    for numerator in range(10,100):
        for denominator in range(numerator+1,100):
            # Reject trivial
            if (numerator % 10 == 0 and denominator % 10 == 0):
                break

            numerator_str = str(numerator)
            denominator_str = str(denominator)
            original_fraction = Fraction(numerator, denominator)

            for n in numerator_str:
                if n in denominator_str:
                    reduced_numerator = int(numerator_str.replace(n, '', 1))
                    reduced_denominator = int(denominator_str.replace(n, '', 1))

                    if reduced_denominator == 0:
                        continue

                    wrong_fraction = Fraction(reduced_numerator, reduced_denominator)

                    if original_fraction == wrong_fraction:
                        print('Found {}/{} = {}/{} (reducing {})'.format(numerator, denominator, reduced_numerator, reduced_denominator, n))
                        result_fraction = result_fraction * original_fraction
                        break

    print('Result: {}/{}'.format(result_fraction.numerator, result_fraction.denominator))


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print('Solved in %.2f seconds' % elapsed)
