n = int(input())
q = list(map(int, input().split()))

arr = [float("inf")] * (n + 1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[b] = min(arr[b], c)

ans = 0
flag = False
for i in range(1, len(arr)):
    if arr[i] == float("inf") and not flag:
        flag = True
    elif arr[i] == float("inf") and flag:
        ans = -1
        break
    else:
        ans += arr[i]
print(ans)