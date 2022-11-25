from functools import lru_cache


t = int(input())

def dp():
    dp = [False] * (n+1)
    dp[0] = True

    for i in range(1, n+1):
        if dp[i-1] and i + seq[i-1] <= n:
            dp[i + seq[i-1]] = True
        if i - seq[i-1] -1 >= 0:
            dp[i] = dp[i] or dp[i-seq[i-1]-1]
    
    return dp[-1]
for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))

    print("YES") if dp() else print("NO")