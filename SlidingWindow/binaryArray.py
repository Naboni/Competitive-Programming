from collections import defaultdict


arr = list(map(int, input().split()))
k = int(input())

def solve(arr, k):
    left = right = 0
    res = 0
    count = defaultdict(int)
    for right in range(len(arr)):
        count[arr[right]] += 1
        while left < len(arr) and count[0] > k:
            count[arr[left]] -= 1
            left += 1
        res = max(res, right-left+1)
    return res

print(solve(arr, k))