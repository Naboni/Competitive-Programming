n, m = map(int, input().split())
arr = []
for i in range(n):
    s = input()
    arr.append(s)
 
ans = ''
for i in range(n):
    for j in range(m):
        count = 0
        for k in range(m):
            if arr[i][j] == arr[i][k]:
                count += 1
 
        for x in range(n):
            if arr[i][j] == arr[x][j]:
                count += 1
 
        if count == 2:
            ans += arr[i][j]
 
print(ans)