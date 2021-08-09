def duplicateZeros(arr):
    pHolder = []
    arrLen = len(arr)
    for j in arr:
        if j == 0:
            pHolder.append(j)
            pHolder.append(j)
        else:
            pHolder.append(j)

    while len(pHolder) != arrLen:
        pHolder.pop()

    arr = pHolder
    print(arr)
duplicateZeros([1,0,2,3,0,4,5,0])
