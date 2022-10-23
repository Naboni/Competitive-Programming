n, k = map(int, input().split())
s = input()

l = 0
res = 0
count = {}
for r in range(n):
    count[s[r]] = count.get(s[r], 0) + 1
    if (r-l+1) - max(count.values()) > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, r-l+1)
print(res)