# arr = [10,2,5,3]
# arr = [7,1,14,11]
# arr = [3,1,7,11]

# Runtime: 64 ms beats 46.96 % of python3 submissions
# Memory Usage: 14.4 MB beats 52.97 % of python3 submissions.
arr = [-2,0,10,-19,4,6,-8]

def checkIfExist(arr):
    arrLen = len(arr)
    pHolder = []

    for i in arr:
        pHolder = arr[::]
        pHolder.remove(i)
        x = i * 2

        for j in pHolder:
            if j == x:
                return True
            
    return False

print(checkIfExist(arr))


# counter = 0
# for i in arr:
#     if 0 in arr:
#         counter += 1
# print(counter)