t = int(input())

def solve(a, b, n):
    if a == n and b == n: return True
    if a + b < n-1: return True
    return False

for _ in range(t):
    n, a, b = map(int, input().split())
    if solve(a, b, n):
        print("Yes")
    else:
        print("No")
