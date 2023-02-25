from cmath import inf
from collections import defaultdict

t = int(input())

def solve(n, arr):
    hashmap = defaultdict(int)
    for el in arr:
        hashmap[el] += 1
    
    vals = list(hashmap.values())
    lst = list(set(vals))
    res = inf
    for i in range(len(lst)):
        cnt = 0
        for j in range(len(vals)):
            if vals[j] > lst[i]:
                cnt += vals[j] - lst[i]
            elif vals[j] < lst[i]:
                cnt += vals[j]
        res = min(res, cnt)
    return res

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(solve(n, arr))