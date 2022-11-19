from functools import lru_cache

n, k, d = map(int, input().split())
MOD = 10**9+7

@lru_cache(None)
def dp(n, incl):
    if n == 0:
        return incl
    res = 0
    for i in range(1, min(k+1, n+1)):
        if i >= d:
            res += dp(n-i, incl or True)
        else:
            res += dp(n-i, incl or False)
    return res % MOD
    
print(dp(n, False))