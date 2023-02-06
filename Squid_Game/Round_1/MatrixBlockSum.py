class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        prefix = mat
        for i in range(n):
            for j in range(m):
                up = mat[i-1][j] if i-1 > -1 else 0
                right = mat[i][j-1] if j-1 > -1 else 0
                both = mat[i-1][j-1] if (i-1 > -1 and j-1 > -1) else 0
                prefix[i][j] = mat[i][j] + up + right - both
        
        ans = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            minrow, maxrow = max(0, i-k), min(i+k, n-1)
            for j in range(m):
                mincol, maxcol = max(0, j-k), min(j+k, m-1)
                ans[i][j] = prefix[maxrow][maxcol]
                if minrow > 0: ans[i][j] -= prefix[minrow-1][maxcol]
                if mincol > 0: ans[i][j] -= prefix[maxrow][mincol-1]
                if minrow > 0 and mincol > 0: ans[i][j] += prefix[minrow-1][mincol-1]
        return ans