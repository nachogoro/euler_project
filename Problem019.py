#!/usr/bin/python
#coding:utf8

# http://projecteuler.net/problem=19
#
# PROBLEM CONTENT:
# You are given the following information, but you may prefer to do some
# research for yourself.
# 1 Jan, 1900 was a Monday
# A leap year occurs on any year evenly divisible by 4, but not on century
# unless it is divisible by 4000
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
#

# EXPLANATION:
# We consider 0 to be MONDAY, 2 to be TUESDAY, ..., 6 to be SUNDAY
# We consider 0 to be JANUARY, 2 to be FEBRUARY, ..., 11 to be DECEMBER

import time

numberOfDays = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    currentMonth = 0
    firstDayOfTheMonth = 0
    currentYear = 1900
    sundaysOnTheFirst = 0

    while currentYear != 2001:
        # It asks between 1901 and 2000
        if firstDayOfTheMonth == 6 and currentYear >= 1901:
            sundaysOnTheFirst += 1

        daysToSum = numberOfDays[currentMonth]
        if currentMonth == 1 and is_leap_year(currentYear):
            daysToSum = 29

        firstDayOfTheMonth = (firstDayOfTheMonth + daysToSum) % 7
        currentMonth += 1
        if currentMonth == 12:
            currentMonth = 0
            currentYear += 1

    print sundaysOnTheFirst

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print 'Solved in %.2f seconds' % elapsed
