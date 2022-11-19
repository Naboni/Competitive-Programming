from collections import defaultdict, deque

n, m = map(int, input().split())
adj = defaultdict(list)

for i in range(m):
		u, v = map(int, input().split())
		adj[u].append(v)
		adj[v].append(u)
visited= set()
ans = 0

def bfs(root):
    if root in visited: 
        return False
    q = deque([root])
    flag = True
    visited.add(root)
    while q:
        node = q.popleft()
        if len(adj[node]) != 2:
            flag=False
        
        for child in adj[node]:
            if child not in visited:
                q.append(child)
                visited.add(child)
    return flag

for i in range(1, n+1):
	ans += bfs(i)
print(ans)