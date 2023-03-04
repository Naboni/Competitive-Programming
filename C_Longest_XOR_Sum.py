n, k = map(int, input().split())
a = list(map(int, input().split()))

pref_xor = [0] * (n+1)
for i in range(n):
    pref_xor[i+1] = pref_xor[i] ^ a[i]

visited = {}
res = 0
for i in range(n+1):
    if pref_xor[i] ^ k in visited:
        res = max(res, i - visited[pref_xor[i] ^ k])
    if pref_xor[i] not in visited:
        visited[pref_xor[i]] = i

print(res)
