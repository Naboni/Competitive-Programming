t = int(input())

def currentDigitsSum(n):
    summ = 0
    while(n):
        summ += n % 10
        n = n // 10
    return summ

def solve(n, s):
    ops = 0
    mult = 10
    while True:
        digits = currentDigitsSum(n)
        if digits <= s:
            break
        else:
            lastn = n % mult
            if lastn != 0:
                n += mult-lastn
                ops += mult - lastn
            mult *= 10
    return ops

for i in range(t):
  n, s = map(int, input().split())
  print(solve(n, s))