arr = list(map(int, input().split()))
k = int(input())

# Don't work for -ve numbers
# def solve(arr, k):
#     left = right = 0
#     summ = 0
#     for right in range(len(arr)):
#         summ += arr[right]
#         while left < len(arr) and summ > k:
#             summ -= arr[left]
#             left += 1
#         if summ == k:
#             return [left, right]
#     return -1
# x, y = solve(arr, k)
# print(*arr[x:y+1])

def doesExist(arr, k):
    sett = set()
    summ = 0
    for num in arr:
        summ += num
        if summ - k in sett:
            return True
        sett.add(summ)
    return False

# print(doesExist(arr, k))

def solve(arr, k):
    mapp = {0:-1}
    summ = 0
    for index in range(len(arr)):
        summ += arr[index]
        if summ - k in mapp:
            return [mapp[summ-k]+1, index+1]
        mapp[summ] = index
    return [None, None]

x = solve(arr, k)
if x[0]:
    print(*arr[x[0]:x[1]])
else: print(-1)