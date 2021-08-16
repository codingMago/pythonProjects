s = "ab"
goal = "ba"

def buddyStrings(s, goal):

    if s == goal:
        return False
    totLen = 0
    for i in s:
        if i in goal:
            totLen += 1
        else:
            return False
    
    if totLen == len(goal):
        return True
    
print(buddyStrings(s, goal))