t = int(input())

for _ in range(t):
    wt, et, ef = map(int, input().split())
    walk = wt * 4
    elev = (ef + 4) * et
    walkandelev = wt*ef + (4-ef)*et
    print(min(walk, elev, walkandelev))