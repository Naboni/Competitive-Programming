from collections import defaultdict, deque

n, k, d = map(int, input().split())
popo = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(n-1):
    u, v = list(map(int, input().split()))
    graph[u].append((v, i + 1))
    graph[v].append((u, i + 1))

keep = set()
dlt = n-1
q = deque(popo)
visited = set(popo)

while q:
    node = q.popleft()
    for nei, idx in graph[node]:
        if nei not in visited:
            q.append(nei)
            visited.add(nei)
            keep.add(idx)
            dlt -= 1

res = []
for i in range(1, n):
    if i not in keep:
        res.append(i)
print(dlt)
print(*res)