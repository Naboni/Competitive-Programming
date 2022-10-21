from functools import lru_cache

n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
@lru_cache
def top_down(summ, index):
    if summ > x or index >= n:
        return 0
    if summ == x:
        return 1
    withCurrCoinAndStay = top_down(summ + coins[index], index)
    withCurrCoinAndLeave = top_down(summ + coins[index], index+1)
    justLeave = top_down(summ, index+1)
    return withCurrCoinAndStay + withCurrCoinAndLeave + justLeave

print(top_down(0, 0))