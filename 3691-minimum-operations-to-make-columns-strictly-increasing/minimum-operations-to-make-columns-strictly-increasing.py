class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        cols = [list(col) for col in zip(*grid)]
        res = 0
        for i in range(len(cols)):
            for j in range(1, len(cols[0])):
                if cols[i][j] <= cols[i][j-1]:
                    val = cols[i][j-1] - cols[i][j] + 1
                    res += val
                    cols[i][j] += val
        return res