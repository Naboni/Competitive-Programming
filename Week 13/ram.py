def ram(n, k, arr):
    arr.sort()
    for i in range(n):
        if arr[i][0] <= k:
            k += arr[i][1]
        else:
            break
    return k
    
t = int(input())
for _ in range(t):
    first = tuple(input().split())
    n, k = int(first[0]), int(first[1])
    second = input().split()
    third = input().split()
    arr = []
    for i in range(n):
        arr.append([int(second[i]), int(third[i])])
    
    print(ram(n, k, arr))
