#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=17
#
# PROBLEM CONTENT:
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used? 
#
#  Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.
#

import time

unitDigits = {0:'',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tenDigits = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
specialDigits = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

# Returns the string representation of a number between 1 and 999
def number_to_string(n):
    result = ''
    lastDigit = n % 10
    twoLastDigits = n % 100
    ten = (n%100) / 10
    hundred = n/100

    if hundred != 0:
        result += unitDigits[hundred]+'hundred'
        if twoLastDigits == 0:
            return result
        else:
            result+='and'

    if ten == 1:
        result += specialDigits[twoLastDigits]
        return result

    if ten == 0:
        result += unitDigits[lastDigit]
        return result

    result += tenDigits[ten] + unitDigits[lastDigit]
    return result


def main():
    # Initialise to 'one thousand'
    sum = 11

    for i in xrange(1, 1000):
        sum += len(number_to_string(i))

    print sum

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
