import sys

# print(sys.getsizeof(int))
# print(sys.getsizeof(float))
# print(sys.getsizeof(list))
# print(sys.getsizeof(tuple))
# print(sys.getsizeof(dict))
# print(sys.getsizeof(bool))

# print(type(int))

x = 1_000_000_000
xsize = sys.getsizeof(x)
y = 10_000_000_000
ysize = sys.getsizeof(y)
print(f"X : {x}, memoryUsage: {xsize}B")
print(f"Y : {y}, memoryUsage: {ysize}B")