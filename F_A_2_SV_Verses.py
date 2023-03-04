# n, a, b = map(int, input().split())
# arr = list(map(int, input().split()))

# res = 0
# sums = [0] * (n+1)
# for i in range(n):
#     sums[i+1] = sums[i] + arr[i]
#     for j in range(i+1):
#         if a <= sums[i+1] - sums[j] <= b:
#             res += 1

# print(res)

n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
prefix_sum = [0] * (n+1)
j = 0
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]
    while j <= i and prefix_sum[i+1] - prefix_sum[j] > b:
        j += 1
    count += i - j + 1
    while j <= i and prefix_sum[i+1] - prefix_sum[j] < a:
        j += 1

print(count)
