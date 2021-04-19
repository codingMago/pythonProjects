# Runtime: 16 ms, faster than 99.83% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.3 MB, less than 33.75% of Python3 online submissions for Defanging an IP Address.

addr = "192.168.0.1"

def defangIPaddr(address):
    pHolder = []
    for i in address:
        if i == ".":
            pHolder.append("[.]")
        else:
            pHolder.append(i)
    
    address = ""
    address = address.join(pHolder)
    return address

print(defangIPaddr(addr))




# Runtime: 28 ms, faster than 77.54% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.3 MB, less than 33.75% of Python3 online submissions for Defanging an IP Address.

addr = "192.168.0.1"

def defangIPaddre(address):
    address = address.replace(".", "[.]")

    return address

print(defangIPaddre(addr))

