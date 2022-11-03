num = int(input())

result = [[1 for _ in range(i)] for i in range(1, num+1)]

for i in range(2, num):
    for j in range(1, i):
        result[i][j] = result[i-1][j-1] + result[i-1][j]

print(result)