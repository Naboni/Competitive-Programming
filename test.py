# def f(n, x, y):
#     reff = [x, y]
#     for i in range(2, 6):
#         reff.append(reff[i-1]-reff[i-2])
#     print(reff)
#     res = reff[n%6]
#     return res

# print(f(0, 0, 1))
# print(f(1, 0, 1))
# print(f(2, 0, 1))
# print(f(3, 0, 1))
# print(f(6, 0, 1))

from collections import defaultdict


n, m = map(int, input().split())
grid = []
for _ in range(m):
    grid.append(list(map(int, input().split())))

players = defaultdict(set)
half = n//2
for i in range(m):
    for j in range(half):
        if len(players[grid[i][j]]) == n-1: continue
        for x in range(half, n):
            players[grid[i][j]].add(grid[i][x])
            players[grid[i][x]].add(grid[i][j])

# print(players)
count = 0
for player in players:
    if len(players[player]) == n-1:
        count += 1
print(n == count)