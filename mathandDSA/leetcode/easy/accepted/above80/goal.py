
s = "G()(al)"

def interpret(command):
    
    dictio = {"G":"G", "()":"o", "(al)":"al"}
    output = []
    pHolder = []

    for i in command:
        pHolder += i

        if pHolder in dictio:
            output.append(dictio[pHolder])
            pHolder = ""

    return "".join(output)
            
print(interpret(s))

# Runtime: 26 ms, faster than 86.08% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.2 MB, less than 66.61% of Python3 online submissions for Goal Parser Interpretation.

# s = "G()(al)"

# def interpret(command):
    
#     dictio = {"G":"G", "()":"o", "(al)":"al"}
#     output = []
#     pHolder = ""

#     for i in command:
#         pHolder += i

#         if pHolder in dictio:
#             output.append(dictio[pHolder])
#             pHolder = ""

#     return "".join(output)
            
# print(interpret(s))

# Runtime: 46 ms, faster than 20.00% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.1 MB, less than 88.17% of Python3 online submissions for Goal Parser Interpretation.

# s = "G()(al)"

# def interpret(command):
    
#     dictio = {"G":"G", "()":"o", "(al)":"al"}
#     output = ""
#     pHolder = ""
    
#     for i in command:
#         pHolder += i
        
#         if pHolder in dictio:
#             output += dictio[pHolder]
#             pHolder = ""
    
#     return output
            
# print(interpret(s))