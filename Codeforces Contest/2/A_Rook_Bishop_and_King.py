r1, c1, r2, c2 = map(int, input().split())

if (r1,c1) == (r2, c2):
    print("0 0 0")
else:
    if r1 == r2 or c1 == c2:
        rook = 1
    else:
        rook = 2
    x, y = abs(r1 - r2), abs(c1 - c2)
    king = max(x, y)
    bishop = 0
    if ((r1+c1)%2 != (r2+c2)%2):
        bisohp = 0
    elif (r1+c1) == (r2+c2):
        bishop = 1
    elif x == y:
        bishop = 1
    else:
        bishop = 2
    print(f"{rook} {bishop} {king}")