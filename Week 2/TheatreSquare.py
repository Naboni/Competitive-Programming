import math
arr = input().split()
m = int(arr[0])
n = int(arr[1])
a = int(arr[2])
def theatreSquare(m, n, a):
    topSide = math.ceil(n/a)
    leftSide = math.ceil(m/a)
    return topSide*leftSide
print(theatreSquare(m,n,a))
