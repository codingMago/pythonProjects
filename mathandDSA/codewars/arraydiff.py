a = [1,2,2,2,3]
b = [2]

def array_diff(a, b):
    for i in b:
        while i in a:
            for j in range(len(a)):
                if a[j] == i:
                    a.pop(j)
                    break
    
    return a

print(array_diff(a, b))