class LRUCache:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
        self.keys = {}
        self.tracker = []

    def get(self, key: int) -> int:
        
        if key in self.keys:
            self.tracker.append(key)
            return self.keys[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.keys: # Update value of key if it exists
            self.keys[key] = value
            self.tracker.append(key)
        else: # Add key:value pair to cache
            if len(self.keys) == self.capacity:    
                self.keys.pop(self.tracker[-1])
                # self.keys.pop() # Pop the least recently used
            self.keys[key] = value
            self.tracker.append(key)
    

[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2) # {}
obj.put(1,1) # {1:1}
obj.put(2,2) # {1:1, 2:2}
print(obj.keys)
# print(obj.get(1)) # return 1
obj.put(3,3) # {1:1, 3:3}
print(obj.keys)
# print(obj.get(2)) # return null
obj.put(4,4) # 
print(obj.keys)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
# expected: 1,-1,-1,3,4
# param_1 = obj.get(key)
# obj.put(key,value)


# dict = {1:2, 2:3, 3:5, 4:1}
# arr = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

# def counter(arr):
#     dic = { }
#     counter = 0
#     highNum = 0

#     arr = sorted(arr)
#     holderArray = []

#     for i in arr:
#         if i not in dic:
#             highNum = 1
#         else:
#             highNum += 1

#         dic[i] = highNum

#     leastUsed = min(dic, key=dic.get)
#     for i in range(len(arr)):
#         if arr[i] != leastUsed:
#             holderArray.append(arr[i])

#     print(f"LeastUsed key: {leastUsed}")
#     print(f"Cleaned array: {holderArray}")

# Keep track of least recently used variable
# Variable that has the least uses recently
# def counter(self):
#     dic = { }
#     counter = 0
#     highNum = 0
#     arr = sorted(self.tracker)
#     holderArray = []

#     for i in arr:
#         if i not in dic:
#             highNum = 1
#         else:
#             highNum += 1

#         dic[i] = highNum

#     leastUsed = min(dic, key=dic.get)
#     for i in range(len(arr)):
#         if arr[i] != leastUsed:
#             holderArray.append(arr[i])

#     self.tracker = holderArray
#     return leastUsed
# counter(arr)