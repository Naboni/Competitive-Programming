class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        block, row, col, blanks = defaultdict(set), defaultdict(set), defaultdict(set), []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[(i//3, j//3)].add(board[i][j])
                else:
                    blanks.append((i, j))
        def backtrack(blanks, ind):
            if ind >= len(blanks):
                return True
            r, c = blanks[ind]
            for k in range(1, 10):
                x = str(k)
                if x not in row[r] and x not in col[c] and x not in block[(r//3, c//3)]:
                    board[r][c] = x
                    row[r].add(x)
                    col[c].add(x)
                    block[(r//3, c//3)].add(x)
                    if backtrack(blanks, ind+1): return True
                    row[r].remove(x)
                    col[c].remove(x)
                    block[(r//3, c//3)].remove(x)
            
        backtrack(blanks, 0)