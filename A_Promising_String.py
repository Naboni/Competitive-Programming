t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = 0
    for i in range(n):
        plus = minus =0
        for j in range(i,n):
            if s[j]=='+':
                plus += 1
            else:
                minus += 1
            if minus >= plus:
                res += 1 if (minus-plus) % 3 == 0 else 0
    print(res)
