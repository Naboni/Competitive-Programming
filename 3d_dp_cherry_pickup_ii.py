from cmath import inf
from functools import lru_cache


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# @lru_cache(None) # Makes you lazy
memo = {}
def topDown(i, j1, j2):
    if j1 < 0 or j2 < 0 or j1 == m or j2 == m: return -inf
    if i == n-1:
        if j1 == j2: return grid[i][j1] 
        else: return grid[i][j1] + grid[i][j2]
    if (i, j1, j2) in memo: return memo[(i, j1, j2)]
    maxi = -inf
    for x in range(-1, 2):
        for y in range(-1, 2):
            nj1, nj2 = j1 + x, j2 + y
            if j1 == j2:
                maxi = max(maxi, grid[i][j1] + topDown(i+1, nj1, nj2))
            else:
                maxi = max(maxi, grid[i][j1] + grid[i][j2] + topDown(i+1, nj1, nj2))
    memo[(i, j1, j2)] = maxi
    return memo[(i, j1, j2)]

# print(topDown(0, 0, m-1))

def bottomUp():
    dp = [[[-inf for _ in range(m)] for _ in range(m)] for _ in range(n)]
    
    for i in range(m):
        for j in range(m):
            if i == j:
                dp[n-1][i][j] = grid[n-1][j]
            else:
                dp[n-1][i][j] = grid[n-1][i] + grid[n-1][j]
    
    for k in range(n-2, -1, -1):
        for j1 in range(m-1, -1, -1):
            for j2 in range(m-1, -1, -1):
                maxi = -inf
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        nj1, nj2 = j1 + x, j2 + y
                        if 0<=nj1<m and 0<=nj2<m:
                            if j1 == j2:
                                maxi = max(maxi, grid[k][j1] + dp[k+1][nj1][nj2])
                            else:
                                maxi = max(maxi, grid[k][j1] + grid[k][j2] + dp[k+1][nj1][nj2])
                dp[k][j1][j2] = maxi

    return dp[0][0][m-1]

print(bottomUp())