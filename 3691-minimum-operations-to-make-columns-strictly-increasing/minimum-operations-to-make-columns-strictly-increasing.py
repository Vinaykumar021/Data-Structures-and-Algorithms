class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        newGrid = [list(cols) for cols in zip(*grid)] 
        res = 0
        for i in range(len(newGrid)):
            for j in range(1, len(newGrid[0])):
                if newGrid[i][j] <= newGrid[i][j-1]:
                    val = newGrid[i][j-1] - newGrid[i][j] + 1
                    res += val
                    newGrid[i][j] += val
        return res

'''  
1.cols = [list(col) for col in zip(*grid)]
Output: Produces a list of lists.
Mutability: Each column is mutable (can be changed).
Use Case: If you need to modify the columns (e.g., increment elements) during your algorithm.
2. cols = list(zip(*grid))
Output: Produces a list of tuples.
Mutability: Each column is immutable (cannot be changed).
Use Case: If you only need to read/access the columns without modifying them.

'''
