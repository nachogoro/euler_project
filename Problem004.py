#!/usr/bin/python

# https://projecteuler.net/problem=4
# Largest palindrome product of two numbers of three digits

def isPalindrome(num):
    return str(num) == str(num)[::-1]

max_palindrome = 0
a = 999
while a >= 100:
    b = 999
    while b >= a:
        if a*b <= max_palindrome:
            break

        if isPalindrome(a*b):
            max_palindrome = a*b

        b = b - 1
    a = a -1

print max_palindrome
