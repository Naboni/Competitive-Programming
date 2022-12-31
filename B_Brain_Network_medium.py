from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(set)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)


def solve(v):
    queue = deque([(v, 0)])
    res = []
    visited = set()
    while queue:
        curr, dist = queue.popleft()
        visited.add(curr)
        res.append((curr, dist))
        for nei in graph[curr]:
            if nei not in visited:
                queue.append((nei, dist + 1))
    
    return res[-1]
    
n1, d1 = solve(1)
n2, d2 = solve(n1)

print(d2) 