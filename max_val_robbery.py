from cmath import inf

weights = list(map(int, input().split()))
values = list(map(int, input().split()))
bag = int(input())
n = len(weights)

memo = {}
def topdown(i, wght):
    if wght > bag: return -inf
    if i == 0: return values[i] if wght + weights[i] <= bag else 0
    if (i, wght) in memo: return memo[(i, wght)]
    memo[(i, wght)] = max(values[i] + topdown(i-1, wght+weights[i]), topdown(i-1, wght))
    return memo[(i, wght)]

print(topdown(n-1, 0))