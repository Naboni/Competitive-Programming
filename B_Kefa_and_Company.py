n, d = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
r = tot = res = 0
for i in range(n):
    while r < n and arr[r][0] - arr[i][0] < d:
        tot += arr[r][1]
        r += 1
    res = max(res, tot)
    tot -= arr[i][1]
print(res)