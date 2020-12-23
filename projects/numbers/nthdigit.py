import math
from decimal import *
getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

def factorial(n):
    if not n:
        return 1
    return n*factorial(n-1)

def get IteratedValue(k):
    k = k+1
    getcontext().prec = k
    sum = 0
    for k in range(k):
        first = factorial()