s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# s = "**|**|***|"
# startIndices = [2,5]
# endIndices = [5,9]
# s = "|**|*|*"
# startIndices = [1,5]
# endIndices = [1,6]
n = len(s)
prev = [-1] * n
next = [-1] * n
prefixSumm = [0] * n
summ = 0
curr = -1
for i in range(n):
    if s[i] == "*":
        summ += 1
    else:
        curr = i
    prefixSumm[i] = summ
    prev[i] = curr
curr = -1
for i in range(n-1, -1, -1):
    if s[i] == "|":
        curr = i
    next[i] = curr

print(prefixSumm)
print(prev)
print(next)
result = []
for s, e in queries:
    left = 0 if next[s] > e else next[s]
    right = 0 if prev[e] < s else prev[e]
    result.append(prefixSumm[right] - prefixSumm[left])
print(result)