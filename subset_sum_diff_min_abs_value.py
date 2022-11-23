arr = list(map(int, input().split()))
n = len(arr)
tot = sum(arr)
memo = {}

# TC: O(n*m*m)
# def topdown(i, s1, s2):
#     if i >= n: return abs(s1 - s2)
#     if (i, s1, s2) in memo: return memo[(i, s1, s2)]
#     memo[(i, s1, s2)] = min(topdown(i+1,s1 + arr[i], s2), topdown(i+1,s1, s2 + arr[i]))
#     return memo[(i, s1, s2)]

# print(topdown(0, 0, 0))

# TC: O(n*m)
def topdown(i, s1):
    if i >= n: return abs((tot - s1) - s1)
    if (i, s1) in memo: return memo[(i, s1)]
    memo[(i, s1)] = min(topdown(i+1,s1 + arr[i]), topdown(i+1,s1))
    return memo[(i, s1)]

print(topdown(0, 0))
