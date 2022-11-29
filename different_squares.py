n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

hashmap = set()
for i in range(1, n):
    for j in range(1, m):
        w,x,y,z = grid[i-1][j-1], grid[i-1][j], grid[i][j-1], grid[i][j]
        hashmap.add((w,x,y,z))
print(len(hashmap))