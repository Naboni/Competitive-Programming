t = int(input())

def prefix(arr):
    summ = 0
    pre = [0]
    for i in arr:
        summ += i
        pre.append(summ)
    return max(pre)

for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))
    x = prefix(red)
    y = prefix(blue)
    print(x+y)
