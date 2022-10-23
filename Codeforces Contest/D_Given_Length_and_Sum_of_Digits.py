m, s = map(int, input().split())
def solve():
    if s > m*9 or m > 1 and s < 1:
        print("-1 -1")
    else:
        maxi, mini = s, s
        for i in range(m-1, -1, -1):
            pos = max(0, maxi-9*i)
            if (i == m-1 and maxi and pos == 0):
                pos = 1
            print(pos, end="")
            maxi -= pos
        print(" ", end="")
        ind = m
        while ind != 0:
            pos = min(9, mini)
            print(pos, end="")
            ind -= 1
            mini -= pos
solve()