n, x = map(int, input().split())
coins = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [0] * (x+1)
dp[0] = 1
for i in range(1, x+1):
    for j in range(len(coins)):
        if i-coins[j] >= 0:
            dp[i] += dp[i-coins[j]]
print(dp[x] % MOD)