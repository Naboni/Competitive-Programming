t = int(input())
for _ in range(t):
    n = int(input())
    powers = set(input().split())
 
    for i in range(1, n+1):
        print(max(idx, len(powers)), end=" ")
    print()
