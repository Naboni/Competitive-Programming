import sys, threading
from collections import defaultdict
from functools import lru_cache
s = input()
t = input()

def main():
    n, m = len(s), len(t)
    memo = defaultdict(lambda:-1)
    def dp(i, j):
        if (i, j) in memo: return memo[i,j]
        if i == n:
            memo[i,j] = m - j
            return memo[i,j]
        if j == m:
            memo[i,j] = n - i
            return memo[i,j]
        if s[i] == t[j]:
            ans = dp(i+1, j+1)
            memo[i,j] = ans
            return memo[i,j]
        ans = 1 + min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))
        memo[i,j] = ans
        return memo[i,j]

    print(dp(0, 0))
    # print(memo)
    def log(i, j, d):
        if (i == n and j == m) or (memo[i,j] == 0):
            return

        if i < n and j < m and s[i] == t[j] and memo[i,j] == memo[i+1,j+1]:
            log(i+1,j+1,d)

        elif i < n and j < m and memo[i,j] == memo[i+1,j+1] + 1:
            print("REPLACE", i+d+1, t[j])
            log(i+1,j+1,d)

        elif j < m and memo[i,j] == memo[i,j + 1] + 1:
            print("INSERT", i+d+1, t[  j])
            log(i,j+1,d+1)

        elif (i < n and memo[i,j] == memo[i+1,j] + 1):
            print("DELETE", i+d+1)
            log(i+1,j,d-1)
    log(0, 0, 0)

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
