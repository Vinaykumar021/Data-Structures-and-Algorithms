class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        n = len(matrix[0]) - 1
        row, col = len(matrix) - 1, 0 
        while row >= 0 and col <= n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
        return False 
        

        