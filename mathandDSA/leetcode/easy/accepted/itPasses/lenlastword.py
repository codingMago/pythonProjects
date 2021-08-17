s = "   fly me   to   the moon  "

def lengthOfLastWord(s: str) -> int:
    pHolder = s.split(" ")
    
    while pHolder[-1] == "":
        pHolder.pop()
    return len(pHolder[-1])

print(lengthOfLastWord(s))


# Runtime: 32 ms, faster than 52.89% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.4 MB, less than 35.80% of Python3 online submissions for Length of Last Word.

# s = "   fly me   to   the moon  "

# def lengthOfLastWord(s: str) -> int:
#     pHolder = s.split(" ")
    
#     while pHolder[-1] == "":
#         pHolder.pop()
#     return len(pHolder[-1])

# print(lengthOfLastWord(s))
