n, m = map(int, input().split())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

"""
110 5 112 113 114
210 211 5 213 214
310 311 3 313 314
410 411 412 5 414
5    1  512 3  3
610  4   1 613 614
710  1   2 713 714
810  1   2  1   1
1    1   2  2   2
4    1   4  4  1014

0   0   0   0   0
0   0   0   0   0
0   0   0   0   0
110 0   0   0   114
210 0   0   0   214
310 0   0   113 314
410 0   0   213 414
610 211 112 313 614
710 311 412 613 714
810 411 512 713 1014
"""

def solve(n, m, grid):
    isCrushable = True
    while isCrushable:
        isCrushable = False
        for i in range(n):
            for j in range(m-2):
                val = abs(grid[i][j])
                if val != 0 and abs(grid[i][j+1]) == val and abs(grid[i][j+2]==val):
                    grid[i][j] = grid[i][j+1] = grid[i][j+2] = -val
                    isCrushable = True
        for i in range(m):
            for j in range(n-2):
                val = abs(grid[j][i])
                if val != 0 and abs(grid[j+1][i]) == val and abs(grid[j+2][i])==val:
                    grid[j][i] = grid[j+1][i] = grid[j+2][i] = -val
                    isCrushable = True
        for col in range(m):
            wr = n-1
            for row in range(n-1, -1, -1):
                if grid[row][col] > 0:
                    wr -= 1
                    grid[wr][col] = grid[row][col]
            while wr >= 0:
                wr -= 1
                grid[wr][col] = 0
        return grid

print(solve(n, m, grid))