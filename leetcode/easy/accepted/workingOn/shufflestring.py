holder = "aiohn"
indexers = [3,1,4,2,0]

def restoreString(s, indices) -> str:
    outputString = s
    
    for index, value in enumerate(indices):
        outputString[index] = s[value]
    
    return "".join(outputString)

print(restoreString(holder, indexers))