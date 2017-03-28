'''
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3
NOTE : DO NOT USE LIBRARY FUNCTIONS

'''


def gcd(A, B):
    if A == 0 or B == 0:
        return max(A, B)
    else:
        return gcd(B, A % B)

print gcd(350,136)
print gcd(2,2)
print gcd(2,0)
print gcd(6,9)
print gcd(9,6)
print gcd(101,10)
