from collections import defaultdict


arr = list(map(int, input().split()))
k = int(input())

def solve(arr, k):
    left = right = 0
    mapp = defaultdict(int)
    res = []
    for right in range(len(arr)):
        mapp[arr[right]] += 1
        size = right - left + 1
        if size == k: 
            res.append(len(mapp))
        elif size > k:
            mapp[arr[left]] -= 1
            if mapp[arr[left]] == 0:
                mapp.pop(arr[left])
            left += 1
            res.append(len(mapp))
    return res

print(*solve(arr, k))