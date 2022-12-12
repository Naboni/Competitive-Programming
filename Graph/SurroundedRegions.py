class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in (0, m-1):
                if board[i][j] == "O":
                    self.dfs(i, j, n, m, board)
        for i in range(m):
            for j in (0, n-1):
                if board[j][i] == "O":
                    self.dfs(j, i, n, m, board)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "?":
                    board[i][j] = "O"

    def dfs(self, r, c, n, m, board):
        if r<0 or c<0 or r==n or c==m or board[r][c] != "O": return
        board[r][c] = "?"
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            self.dfs(r+dr, c+dc, n, m, board)