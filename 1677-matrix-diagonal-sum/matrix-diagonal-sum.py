class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, sum = len(mat), 0
        for i in range(n):
            sum += mat[i][i]
            sum += mat[i][n-1-i]
        return sum - (mat[n//2][n//2] if n%2 else 0) 
        