k = int(input())
arr = list(map(int, input().split()))

memo = {}
def dp(i, summ):
    if summ == 0: return True
    if i == 0: return arr[0] == k
    if (i, summ) in memo: return memo[(i, summ)]
    memo[(i, summ)] = dp(i-1, summ-arr[i]) or dp(i-1, summ)
    return memo[(i, summ)]

# print("Yes") if dp(len(arr)-1, k) else print("No")

def bottomup():
    n = len(arr)
    dp = [[False for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    dp[0][arr[0]] = True
    for i in range(1, n):
        for j in range(1, k+1):
            notTake = dp[i-1][j]
            take = False
            if arr[i] <= j:
                take = dp[i-1][j-arr[i]]
            dp[i][j] = take or notTake
    return dp[n-1][k]

print("Yes") if bottomup() else print("No")