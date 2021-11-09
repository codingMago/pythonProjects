arr = [17,18,5,4,6,1]

def replaceElements(arr):

    retHolder = []
    pHolder = arr[::]
    
    for i in arr:

        pHolder.remove(i)

        if pHolder:
            retHolder.append(max(pHolder))
            
        else:
            retHolder.append(-1)

    return retHolder
            
print(replaceElements(arr))

# Runtime: 7776 ms   # Slowest so far
# Memory Usage: 15.5 MB beats 21.26 % of python3 submissions

# arr = [17,18,5,4,6,1]

# def replaceElements(arr):

#     retHolder = []
#     pHolder = arr[::]
    
#     for i in arr:

#         pHolder.remove(i)

#         if pHolder:
#             highest = -500
#             for i in pHolder:
#                 if i > highest:
#                     highest = i
#             retHolder.append(highest)
            
#         else:
#             retHolder.append(-1)

#     return retHolder
            
# print(replaceElements(arr))

# Runtime: 2872 ms beats 32.59 % of python3 submissions
# Memory Usage: 15.7 MB beats 14.88 % of python3 submissions

# arr = [17,18,5,4,6,1]

# def replaceElements(arr):

#     retHolder = []
#     pHolder = arr[::]
    
#     for i in arr:

#         pHolder.remove(i)

#         if pHolder:
#             retHolder.append(max(pHolder))
            
#         else:
#             retHolder.append(-1)

#     return retHolder
            
# print(replaceElements(arr))

# Runtime: 2892 ms beats 32.51 % of python3 submissions
# Memory Usage: 15.5 MB beats 21.26 % of python3 submissions

# arr = [17,18,5,4,6,1]

# def replaceElements(arr):

#     retHolder = []
#     pHolder = arr[::]
    
#     for i in arr:

#         pHolder.remove(i)

#         if len(pHolder) == 0:
#             retHolder.append(-1)

#         else:
#             retHolder.append(max(pHolder))

#     return retHolder
            
# print(replaceElements(arr))
