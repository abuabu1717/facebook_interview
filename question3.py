'''
You are given an array of integers.

Write an algorithm that brings all nonzero elements to the left of the array, and returns the number of nonzero elements.

The algorithm should operate in place, i.e. shouldn't create a new array.

The order of the nonzero elements does not matter. The numbers that remain in the right portion of the array can be anything.

Example:
given the array [ 1, 0, 2, 0, 0, 3, 4 ],
a possible answer is [ 4, 1, 3, 2, ?, ?, ? ], 4 non-zero elements, where "?" can be any number.

Code should have good complexity and minimize the number of writes to the array.


'''
import time
def sortArray(arr):
    count = 0
    wR=0
    while(wR<len(arr)-count):
        if arr[wR]>0 or arr[wR]<0:
            wR += 1
        elif arr[wR]==0:
            count += 1
            arr.append(arr.pop(wR))
    return True

arr = [[-1,0,2,0,0,3,-4],[0,6,8,0,0,1,2,0,0,0,3,7,8,0,0,3,5,0,6,0,0,0],[1,2,3,4,0,0,5,6,7,8],[0,1,2,3,4,5,6,7,8,8]]
start = time.time()
for i in xrange(1000):
    for test in arr:
        sortArray(test)
end = time.time()
print end-start


def newF(arr):
    pos = 0
    for i in xrange(len(arr)):
        if arr[i]!=0:
            arr[pos]=arr[i]
            pos += 1
    for i in reversed(range(pos,len(arr))):
        arr[i]=0
    return True

arr = [[-1,0,2,0,0,3,-4],[0,6,8,0,0,1,2,0,0,0,3,7,8,0,0,3,5,0,6,0,0,0],[1,2,3,4,0,0,5,6,7,8],[0,1,2,3,4,5,6,7,8,8]]
start = time.time()
for i in xrange(1000):
    for test in arr:
        newF(test)
end = time.time()
print end-start