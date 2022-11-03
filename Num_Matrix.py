class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.integral_image = [[0 for _ in range(col+1)] for _ in range(row+1)]
        for i in range(row):
            summ = 0
            for j in range(col):
                summ += matrix[i][j]
                self.integral_image[i+1][j+1] = summ
                if i > 0:
                    self.integral_image[i+1][j+1] += self.integral_image[i][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.integral_image[row2+1][col2+1] - self.integral_image[row1][col2+1] 
                - self.integral_image[row2+1][col1] + self.integral_image[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)