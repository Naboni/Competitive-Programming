from itertools import combinations

n, k = map(int, input().split())
a = list(map(int, input().split()))

pairs = list(combinations(range(2*n), 2))
inf = float('inf')

# dp[i][j] is the minimum time to complete i pairings with students j as the last one paired
dp = [[inf]*(1<<2*n) for _ in range(k+1)]
dp[0][0] = 0

for i in range(1, k+1):
    for j in range(2*n):
        for s in range(1<<2*n):
            if not (s & (1<<j)):
                continue
            for t in range(s^(1<<j)):
                if not (t & (1<<j)):
                    continue
                u = pairs.index((j,t.bit_length()-1))
                dp[i][s] = min(dp[i][s], dp[i-1][t] + max(a[j], a[t.bit_length()-1]) + max(a[pairs[u][0]], a[pairs[u][1]]))

print(dp[k][(1<<(2*n))-1])
