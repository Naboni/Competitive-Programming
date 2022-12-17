t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        ans = max(ans, ord(s[i])-ord("a")+1)
    print(ans)