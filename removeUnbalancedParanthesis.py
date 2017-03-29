'''
Given a string, remove unbalanaced paranthesis
'''

def balance(s):
    myList=[]
    i=0
    while i < len(s):
        if s[i] =='(':
            myList.append([i,'('])
            i+=1
        elif s[i] ==')' :
            if not myList:
                s = s[:i]+s[i+1:]
            else:
                del myList[-1]
                i+=1
        else:
            i+=1
            continue
    if myList:
        for items in range(len(myList)):
            index = myList[items][0]-items
            s = s[:index] + s[index + 1:]
    return s

print balance("((a)b()((()))(b(b()")
print balance("((()")
print balance("(()))")
print balance("()))")
print balance("(dfgh)00)")
print balance("(()()())")
print balance("(((())")