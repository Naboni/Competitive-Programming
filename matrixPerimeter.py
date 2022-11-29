from cmath import inf


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(str, input().split())))


visited = set()
def dfs(i, j):
    if i < 0 or j < 0 or i == n or j == m:
        return 1
    if grid[i][j] == "false":
        return 1
    if (i, j) in visited:
        return 0
    visited.add((i,j))
    res = 0
    for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx, ny = i + x, y + j
        res += dfs(nx, ny)
    return res

for i in range(n):
    for j in range(m):
        if grid[i][j] == "true":
            u,v = i,j
            break
print(dfs(u, v))