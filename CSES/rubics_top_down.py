import sys, threading
from functools import lru_cache

def main():
    n = int(input())
    MOD = 10**9 + 7
    @lru_cache
    def dp(summ):
        if summ > n:
            return 0
        if summ == n:
            return 1
        res = 0
        for i in range(1, 7):
            res += dp(summ + i)
        return res
    print(dp(0) % MOD)

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()