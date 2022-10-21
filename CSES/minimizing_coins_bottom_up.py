from cmath import inf
n, x = map(int, input().split())
coins = list(map(int, input().split()))
dp = [inf] * (x+1)
dp[0] = 0
coins.sort()
for i in range(1, x+1):
    for j in range(len(coins)):
        if i-coins[j] >= 0:
            dp[i] = min(dp[i], 1 + dp[i-coins[j]])
print(dp[x] if dp[x] != inf else -1)