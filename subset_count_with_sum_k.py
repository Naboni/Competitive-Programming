arr = list(map(int, input().split()))
k = int(input())
n = len(arr)

memo = {}
def topdown(i, s):
    if s == 0: return 1
    if s < 0 or i < 0: return 0
    if (i, s) in memo: return memo[(i, s)]
    memo[(i, s)] = topdown(i-1, s-arr[i]) + topdown(i-1, s)
    return memo[(i, s)]

print(topdown(n-1, k))