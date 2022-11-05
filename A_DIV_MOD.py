tests = int(input())

def solve(left, right, a):
    div = right // a
    mod = right % a
    res = div + mod
    prev = (div-1) * a + (a-1)
    # x = (div-1) * a + (a-1)
    # prev = right - 1
    # print(x, prev)
    if prev >= left:
        tmp = (div-1) + (a-1)
        res = max(res, tmp)
    return res

for _ in range(tests):
    left, right, a = map(int, input().split())
    print(solve(left, right, a))