from collections import deque


grid = []
n, m = map(int, input().split())

for i in range(n):
    grid.append(list(map(str, input().split())))

for i in range(n):
    for j in range(m):
        if grid[i][j] == "*":
            start = (i, j)
        elif grid[i][j] == "O":
            end = (i, j)

def bfs():
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    while queue:
        r, c, dist = queue.popleft()
        if grid[r][c] == "#":
            return dist
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = dx + r, dy + c
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] != "X":
                queue.append((nx, ny, dist+1))
                visited.add((nx, ny))
    return -1

print(bfs())