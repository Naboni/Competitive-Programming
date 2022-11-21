n = int(input())
meets = []
for _ in range(n):
    meets.append(list(map(int, input().split())))

meets.sort(key=lambda x:x[1])

res = 1
for i in range(1, n):
    if meets[i][0] < meets[i-1][1]:
        res += 1
print(res)
