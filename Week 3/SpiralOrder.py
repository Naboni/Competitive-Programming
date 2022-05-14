class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top  = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        notDone = True
        spiral = []
        while top <= bottom and left <= right and notDone:
            for i in range(left, right+1):
                spiral.append(matrix[top][i])
            if top < bottom:
                for j in range(top+1, bottom+1):
                    spiral.append(matrix[j][right])
                for k in range(right-1, left-1,-1):
                    spiral.append(matrix[bottom][k])
            else:
                notDone = False
            if left < right:
                for l in range(bottom-1, top, -1):
                    spiral.append(matrix[l][left])
            else:
                notDone = True
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return spiral
