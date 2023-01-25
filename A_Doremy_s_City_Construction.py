t = int(input())

for k in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            ans = max(ans, (i+1)*(n-i-1))
    print(n//2) if ans == 0 else print(ans)