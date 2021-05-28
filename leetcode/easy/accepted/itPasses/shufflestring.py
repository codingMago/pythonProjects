# Runtime: 76 ms, faster than 5.62% of Python3 online submissions for Shuffle String.
# Memory Usage: 14.3 MB, less than 21.04% of Python3 online submissions for Shuffle String.
# Ran at 32 and 34 in testcases, on submission it more than doubled
# But it runs

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

def restoreString(s, indices) -> str:
    retStr = ""
    enumerator = 0
    totLength = len(indices)

    while indices:
        for i in range(totLength): # Fill in our dictionary
            if indices[i] == enumerator:
                retStr += s[i]
                indices.pop(i)
                s = s[:i] + s[i+1:]
                enumerator += 1
                totLength -= 1
                break


    return retStr

print(restoreString(s, indices))
