'''

Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

Note that since Java does not have unsigned int, use long for Java
'''
#Better solution
def newSol(A):
    ret = 0
    while A != 0:
        if A&1:
            ret += 1
        A=A>>1
    return ret
print newSol(32)
print newSol(11)


def numSetBits(A):
    binary = str((bin(A))[2:])
    count = 0
    for char in binary:
        count += int(char) & 1
    return count

print numSetBits(32)

