from collections import Counter

n = int(input())

pts = []
for _ in range(n):
    pts.append(tuple(map(int, input().split())))

mapp = Counter(pts)

res = 0
for key in mapp:
    for i in range(-2, 3):
        for j in range(-2, 3):
            x, y = key[0] + i, key[1] + j 
            if (x,y) == key:
                if mapp[key] >= 2:
                    res += mapp[key] * (mapp[key] - 1)
            else:
                res += mapp[(x,y)] * mapp[key]
print(res//2)
