from cmath import inf
import sys, threading
# n = int(input())
# energy = list(map(int, input().split()))

# words = []
# for _ in range(n):
#     s = input()
#     words.append(s)

# dp = [[inf] * 2 for _ in range(n)]
# dp[0][0] = 0
# dp[0][1] = energy[0]
# for i in range(1, n):
#     for j in range(2):
#         res = inf
#         x = 0
#         word = words[i]
#         if j == 1:
#             x = energy[i]
#             word = word[::-1]
#         for k in range(2):
#             prev = words[i - 1]
#             if k == 1:
#                 prev = prev[::-1]
#             if prev <= word:
#                 res = min(res, x + dp[i - 1][k])
#             else:
#                 res = min(res, inf)
#         dp[i][j] = res

# ans = min(dp[n - 1][0], dp[n - 1][1])
# if ans == inf:
#     print(-1)
# else:
#     print(ans)

from cmath import inf
from functools import lru_cache
 
def main():
    n = int(input())
    energy = list(map(int, input().split()))
    
    words = []
    for _ in range(n):
        s = input()
        words.append(s)

    @lru_cache(None)
    def dp(i, j):
        if i == 0 and j == 0: return 0
        if i == 0 and j == 1: return energy[0]
        res = inf
        x = 0
        word = words[i]
        if j == 1:
            x = energy[i]
            word = word[::-1]
        for k in range(2):
            prev = words[i - 1]
            if k == 1:
                prev = prev[::-1]
            if prev <= word:
                res = min(res, x + dp(i - 1,k))
            else:
                res = min(res, inf)
        return res
    
    ans = min(dp(n - 1, 0), dp(n - 1, 1))
    if ans == inf:
        print(-1)
    else:
        print(ans)

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()