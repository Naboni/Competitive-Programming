arr = list(map(int, input().split()))
diff = int(input())
n = len(arr)
tot = sum(arr)
memo = {}

def topdown(i, s1):
    if i >= n: return abs((tot-s1) - s1) == diff
    if (i, s1) in memo: return memo[(i, s1)]
    memo[(i, s1)] = topdown(i+1, s1+arr[i]) + topdown(i+1, s1)
    return memo[(i, s1)]

print(topdown(0, 0))