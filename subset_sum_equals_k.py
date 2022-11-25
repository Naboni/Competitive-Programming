from functools import lru_cache


k = int(input())
arr = list(map(int, input().split()))

# memo = {}
@lru_cache(None)
def dp(i, summ):
    if summ < 0: return False
    if summ == 0: return True
    if i == 0: return arr[0] == k
    return dp(i-1, summ-arr[i]) or dp(i-1, summ)

# print("Yes") if dp(len(arr)-1, k) else print("No")
# n -> 0
# t -> 0

def bottomup():
    
    n = len(arr)
    dp = [[False] * (k +1) for _ in range(n)]
    for i in range(len(dp)):
        for summ in range(len(dp[0])):
            if summ == 0:
                dp[i][summ] = True
                continue
            if i == 0: 
                dp[i][summ] = arr[0] == k
                continue

            dp[i][summ] =  dp[i-1][summ]
            if not (summ-arr[i] < 0):
                dp[i][summ] |= dp[i-1][summ-arr[i]]

    return dp[len(arr)-1][k]
    
print("Yes") if bottomup() else print("No")
    # dp = [[False for _ in range(k+1)] for _ in range(n)]
    # for i in range(n):
    #     dp[i][0] = True
    # dp[0][arr[0]] = True
    # for i in range(1, n):
    #     for j in range(1, k+1):
    #         notTake = dp[i-1][j]
    #         take = False
    #         if arr[i] <= j:
    #             take = dp[i-1][j-arr[i]]
    #         dp[i][j] = take or notTake
    # return dp[n-1][k]

# print("Yes") if bottomup() else print("No")