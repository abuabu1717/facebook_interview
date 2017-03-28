'''

# There's a room with a TV and people are coming in and out to watch it. The TV is on only when there's at least a person in the room.
# For each person that comes in, we record the start and end time. We want to know for how long the TV has been on. In other words:
# Given a list of arrays of time intervals, write a function that calculates the total amount of time covered by the intervals.
# For example:

# input = [(1,4), (2,3)]
# > 3
# input = [(4,6), (1,2)]
# > 3
# input = {{1,4}, {6,8}, {2,4}, {7,9}, {10, 15}}
# > 11

'''

def timeInterval(arr):
    arr.sort()
    count = 0
    wR = 0
    while wR<len(arr):
        try:
            if arr[wR+1][0]>=arr[wR][1]:
                count = count + arr[wR][1]-arr[wR][0]
                wR += 1
            else:

        except:
            count += arr[wR][1]-arr[wR][0]
            wR+=1
        #if arr[wR+1][0]>=arr[wR][0] and arr[wR+1][0]<arr[wR][1]:
         #   if arr[wR+1][1]>=arr[wR][1]:
    return count


arr = [(1, 4), (2, 4), (6, 8), (7, 9), (10, 15), (1, 5), (1, 3)]
arr=[(1,4),(2,3),(4,6)]
#[(1, 3), (1, 4), (1, 5), (2, 4), (6, 8), (7, 9), (10, 15)]
print timeInterval(arr)