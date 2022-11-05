tests = int(input())

def solve(n, k, arr):
    rem = [0] * n
    for i in range(n):
        if arr[i] % k:
            rem[i] = k - (arr[i] % k)
    # print(rem)
    rem.sort()
    # print(rem)
    count = 1
    for i in range(n-1):
        if rem[i] == rem[i+1] and rem[i] != 0:
            rem[i] += count * k
            count += 1
        else:
            count = 1
    # print(rem)
    res = max(rem)
    return 0 if not res else res + 1
    

for _ in range(tests):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(n, k, arr))