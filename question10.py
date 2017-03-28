arr = [900, 940, 950, 1100, 1500, 1800]
dep= [910, 1200, 1120, 1130, 1900, 2000]

def numberOfGates(arr,dep):
    result = 0
    plat_needed = 0
    i=0
    j=0
    n=len(arr)
    while (i<n) and (j<n):
        if arr[i]<dep[j]:
            plat_needed += 1
            i += 1
            result = max(result,plat_needed)
        else:
            plat_needed -=1
            j +=1
    return result

print numberOfGates(arr,dep)


