'''

Question: Given a sequence of positive integers A and an integer T, return whether there is a continuous sequence of A that sums up to exactly T
Example
[23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20
[1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8
[1, 3, 5, 23, 2], 7 Return False because no sequence in this array adds up to 7


'''

def checkSum(arr,T):
    wL=0
    wR=0
    total = arr[0]
    while wL<len(arr)-1:
        if total<T:
            wR +=1
            total += arr[wR]
        if total == T:
            return True
        if total > T:
            total -= arr[wL]
            wL+=1
    return False



arr=[23,5,4,7,2,11]
print checkSum(arr,20) #True
print checkSum([1, 3, 5, 23, 2], 8) #True
print checkSum([1, 3, 5, 23, 2], 7) #False