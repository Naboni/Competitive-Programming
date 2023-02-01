from cmath import inf
from math import ceil

t = int(input())

def solve(n, arr):
    l, r = 0, inf
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            l = max(l, ceil((arr[i-1]+arr[i])/2))
        elif arr[i-1] < arr[i]:
            r = min(r, (arr[i-1]+arr[i])//2)
    return l if l <= r else -1

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))