# Runtime: 36 ms, faster than 97.65% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.2 MB, less than 59.58% of Python3 online submissions for Roman to Integer.

# Gotta go fast

s = "III"

def romantoint(s):
    pHolder = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    counter = 0
    prev = ""

    if len(s) == 0:
        return False

    for i in s:
        if prev == "I":
            if i == "V":
                counter += 3 # Account for previous 1
            elif i == "X":
                counter += 8 # Account for previous 1
            else:
                counter += pHolder[i]
        elif prev == "X":
            if i == "L":
                counter += 30 # Account for previous 10
            elif i == "C":
                counter += 80 # Account for previous 10
            else:
                counter += pHolder[i]
        elif prev == "C":
            if i == "D":
                counter += 300 # Account for previous 100
            elif i == "M":
                counter += 800 # Account for previous 100
            else:
                counter += pHolder[i]
        else:
            counter += pHolder[i]
        
        prev = i
    
    return counter

print(romantoint(s))



# Runtime: 48 ms, faster than 63.50% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.3 MB, less than 59.58% of Python3 online submissions for Roman to Integer.

# s = "LVIII"

# def romantoint(s):
#     pHolder = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

#     counter = 0
#     prev = ""

#     if len(s) == 0:
#         return False

#     for i in s:
#         if i == "V" and prev == "I":
#             counter += 3 # Account for previous 1
#         elif i == "X" and prev == "I":
#             counter += 8 # Account for previous 1
#         elif i == "L" and prev == "X":
#             counter += 30 # Account for previous 10
#         elif i == "C" and prev == "X":
#             counter += 80 # Account for previous 10
#         elif i == "D" and prev == "C":
#             counter += 300 # Account for previous 100
#         elif i == "M" and prev == "C":
#             counter += 800 # Account for previous 100
#         else:
#             counter += pHolder[i]
        
#         prev = i
    
#     return counter

# print(romantoint(s))

