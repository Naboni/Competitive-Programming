def solve(li):
    zc, oc = 0, 0
    ans = 0
    for i in li:
        if i == 0:
            zc += 1
            ans += oc
        else:
            oc += 1
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = solve(arr)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = 1
            ans = max(ans, solve(arr))
            arr[i] = 0
            break
    for i in range(n-1, -1, -1):
        if arr[i] == 1:
            arr[i] = 0
            ans = max(ans, solve(arr))
            arr[i] = 1
            break
    print(ans)