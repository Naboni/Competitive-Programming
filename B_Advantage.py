t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr=sorted(arr)
    a=sorted_arr[-1]
    b=sorted_arr[-2]
    res = []
    for el in arr:
        print(el-a if el!=a else el-b, end=' ')
    print()