from cmath import inf
from functools import lru_cache

n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
@lru_cache
def top_down(summ, index):
    if summ > x or index >= len(coins):
        return inf
    if summ == x:
        return 0
    includeAndStay = 1 + top_down(summ + coins[index], index)
    includeAndLeave = 1 + top_down(summ + coins[index], index+1)
    justLeave = top_down(summ, index+1)
    return min(includeAndStay, includeAndLeave, justLeave)

print(top_down(0, 0))