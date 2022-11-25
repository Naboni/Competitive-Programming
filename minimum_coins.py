from cmath import inf


coins = list(map(int, input().split()))
amount = int(input())
n = len(coins)

memo = {}
def topdown(i, summ):
    if summ == 0: return 0
    if summ < 0 or i < 0: return inf
    if (i, summ) in memo: return memo[(i, summ)]
    memo[(i, summ)] = min(1 + topdown(i, summ-coins[i]), topdown(i-1, summ))
    return memo[(i, summ)]

print(topdown(n-1, amount))