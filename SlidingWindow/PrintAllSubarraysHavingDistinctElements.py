from collections import defaultdict


arr = list(map(int, input().split()))

def solve(arr):
    mapp = defaultdict(int)
    left = 0
    res = []
    for right in range(len(arr)):
        mapp[arr[right]] += 1
        if mapp[arr[right]] == 2:
            res.append((left, right))
        while left < right and mapp[arr[right]] > 1:
            mapp[arr[left]] -= 1
            left += 1
    res.append((left, right+1))
    return res

ans = solve(arr)
for x, y in ans:
    print(*arr[x:y])