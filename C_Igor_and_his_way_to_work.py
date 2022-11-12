from cmath import inf
from collections import deque

n, m = map(int, input().split())
grid = [[i for i in input()] for _ in range(n)]

directions = [(1,0),(0,1),(-1,0),(0,-1)]

def solve(n, m, grid):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                start = (i, j)
    queue = deque()
    for dr, dc in directions:
        queue.append(((start, (dr, dc), 0)))
    visited = [[inf for _ in range(m)] for _ in range(n)]
    while queue:
        pos, dir, turns = queue.popleft()
        if grid[pos[0]][pos[1]] == "T" and turns <= 2:
            return True
        if turns > 2:
            continue
        for dr, dc in directions:
            nr, nc = pos[0] + dr, pos[1] + dc
            if 0<=nr<n and 0<=nc<m and grid[nr][nc] != "*" and visited[nr][nc] >= turns+1:
                if dir == (dr, dc):
                    queue.append(((nr, nc), (dr, dc), turns))
                    visited[nr][nc] = turns
                else:
                    queue.append(((nr, nc), (dr, dc), turns + 1))
                    visited[nr][nc] = turns + 1

    return False

if solve(n, m, grid):
    print("YES")
else:
    print("NO")