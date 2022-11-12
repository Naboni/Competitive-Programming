t = int(input())

for _ in range(t):
    n, curr = map(str, input().split())
    light = input()
    light = light * 2
    res = 0
    l = 0
    for i in light[::-1]:
        l += 1
        if i == 'g':
            l = 0
        if i == curr:
            res = max(res, l)
    print(res)