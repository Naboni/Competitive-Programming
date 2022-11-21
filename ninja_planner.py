n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

dp = [[-1 for _ in range(m+1)] for _ in range(n)]

def topDown(day, last):
    if dp[day][last] != -1: dp[day][last]
    if day == 0:
        maxi = 0
        for i in range(m):
            if i != last:
                maxi = max(maxi, grid[0][i])
        return maxi
    
    res = 0
    for i in range(m):
        if i != last:
            res = max(res, grid[day][i] + topDown(day-1, i))
    dp[day][last] = res
    return dp[day][last]

# print(topDown(n-1, m))

def bottomUp():
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    dp[0] = grid[0]

    for i in range(1, n):
        for j in range(m):
            maxi = 0
            for k in range(m):
                if k != j:
                    maxi = max(maxi, dp[i-1][k])
            dp[i][j] = grid[i][j] + maxi
    
    return max(dp[-1])

print(bottomUp())