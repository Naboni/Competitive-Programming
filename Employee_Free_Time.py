n = int(input())

times = []
for _ in range(n):
    i = int(input())
    emp = []
    for _ in range(i):
        emp.append(list(map(int, input().split())))
    times.append(emp)

merged = []
for e in times:
    for i in e:
        merged.append(i)
# print(merged)
m = sorted(merged, key=lambda x:x[1])
# print(m)
x = [m[0]]
for i in range(len(m)):
    if m[i][0] < x[-1][1]:
        x[-1][1] = max(m[i][1], x[-1][1])
        x[-1][0] = min(m[i][0], x[-1][0])
    else:
        x.append(m[i])
# print(x)
res = []
for i in range(1, len(x)):
    res.append([x[i-1][1], x[i][0]])
print(*res)