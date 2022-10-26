tests = int(input())

for _ in range(tests):
    n, k = map(int, input().split())
    goods = list(map(int, input().split()))

    modded_goods = []
    for i in range(n):
        modded_goods.append(goods[i] % k)
    modded_goods.sort()
    left, right = 0, n-1
    remain = 0
    while left < n and right > left:
        x = modded_goods[left] + modded_goods[right]
        if x == k:
            left += 1
            right -= 1
        elif x < k:
            remain += modded_goods[left]
            left += 1
        elif x > k:
            remain += (x % k)
            left += 1
            right -= 1
    print((sum(goods) - remain) // k)