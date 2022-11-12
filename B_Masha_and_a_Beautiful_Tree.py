t = int(input())

def solve(m, perm):
    i = 1
    res = 0
    while i < m:
        op = 0
        step = 2 * i
        for j in range(0,m,step):
            if perm[j] > perm[j+i]:
                op += 1
                perm[j:j+i], perm[j+i:j+step] = perm[j+i:j+step], perm[j:j+i]
        res += op
        i *= 2
    for k in range(m):
        if perm[k] != k+1:
            return -1
    return res

for _ in range(t):
    m = int(input())
    perm = list(map(int, input().split()))
    print(solve(m, perm))
