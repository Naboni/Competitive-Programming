n = int(input())
s = input()
cost = list(map(int, input().split()))


def solve():
    dp = [0] * 4
    for i in range(n):
        if s[i] == "h":
            dp[0] += cost[i]
        elif s[i] == "a":
            dp[1] = min(dp[0], dp[1] + cost[i])
        elif s[i] == "r":
            dp[2] = min(dp[1], dp[2] + cost[i])
        elif s[i] == "d":
            dp[3] = min(dp[2], dp[3] + cost[i])
    return dp[-1]

print(solve())