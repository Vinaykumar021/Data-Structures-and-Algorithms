class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visit = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if (r not in range(rows)
            or c not in range(cols)
            or(r, c) in visit
            or grid[r][c] == "0"):
                return
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands

