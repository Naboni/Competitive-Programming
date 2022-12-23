from collections import Counter


arr = list(map(int, input().split()))
freq = Counter(arr)
x = (sorted(freq.items(), key=lambda x:[x[1], -x[0]]))
res = []
for i, j in x:
    for k in range(j):
        res.append(i)
print(*res)