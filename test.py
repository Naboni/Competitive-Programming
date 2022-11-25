dp = [False]*n
dp = [True] + dp
for i in range(1, n + 1):
    if dp[i - 1] and i + a[i - 1] <= n:
        dp[i + a[i - 1]] = True
    if i - a[i - 1] - 1 >= 0:
        dp[i] |= dp[i - a[i - 1] - 1]

if dp[-1]:
    print('YES')
else:
    print('NO')