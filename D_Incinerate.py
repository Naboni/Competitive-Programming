def solve(n, k, hp, pwr):
    arr = []
    for i in range(n):
        arr.append([pwr[i], hp[i]])
    arr.sort()
    print(arr)
    curr = k
    flag = True
    for p, h in arr:
        while h - curr > 0 and k > 0:
            k -= p
            curr += k
        if k <= 0:
            flag = False
            break
    return flag


for _ in range(int(input())):
    n, k = map(int, input().split())
    hp = list(map(int, input().split()))
    pwr = list(map(int, input().split()))
    print("YES" if solve(n, k, hp, pwr) else "NO")