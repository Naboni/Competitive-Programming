s = input()

def solve(s):
    n = len(s)
    upper = lower = 0
    x = 0
    res = 0
    for i in range(n-1, -1, -1):
        if s[i].islower():
            lower += 1
        if s[i].isupper():
            upper += 1
            x += 1
        elif x > 0:
            x -= 1
            res += 1
    return min(res, lower, upper)

print(solve(s))