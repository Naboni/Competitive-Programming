class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMatrix = [[0]* (cols+1) for _ in range(rows+1)]
        for i in range(rows):
            prefix = 0
            for j in range(cols):
                prefix += matrix[i][j]
                above = self.sumMatrix[i][j+1]
                self.sumMatrix[i+1][j+1] = prefix + above 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1
        total = self.sumMatrix[row2][col2]
        left = self.sumMatrix[row2][col1-1]
        top = self.sumMatrix[row1-1][col2]
        topLeft = self.sumMatrix[row1-1][col1-1]
        return total - top - left + topLeft 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
