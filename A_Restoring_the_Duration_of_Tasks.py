t = int(input())

for _ in range(t):
    n = int(input())
    begin = list(map(int, input().split()))
    end = list(map(int, input().split()))

    res = []
    for i in range(n):
        if i == 0:
            ans = end[i] - begin[i]
        else:
            ans = end[i] - min(max(begin[i], end[i-1]), end[i])
        res.append(ans)
    print(*res)