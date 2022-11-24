from collections import deque

r, c = map(int, input().split())
visited = set([(0,0)])
def bfs():
    queue = deque([(0,0,0)])
    while queue:
        i, j, dist = queue.popleft()
        if (i, j) == (r, c):
            return dist
        for dr, dc in [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]:
            nr, nc = i + dr, j + dc
            if (nr, nc) not in visited:
                queue.append((nr, nc, dist+1))
                visited.add((nr, nc))
    return -1
print(bfs())