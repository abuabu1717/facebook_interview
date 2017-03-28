'''
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.

'''

def majorityElement(A):
    majority_idx = 0
    count = 1
    n = len(A)
    for i in range(1, n):
        if A[majority_idx] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_idx = i
            count = 1
    ret = A[majority_idx]
    count = 0
    for a in A:
        if a == ret:
            count += 1
    if count >= n / 2:
        return ret
    return -1


A=[2,1,2]
print majorityElement(A)