from math import ceil

t = int(input())

def solve(n, arr):
    summ = 0
    maxi = max(arr)
    for el in arr:
        summ += el
        maxi = max(el, maxi)
    num = max(maxi, ceil(summ/(n-1)))
    rqrd = num * (n-1)
    diff = rqrd - summ
    return diff

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))
