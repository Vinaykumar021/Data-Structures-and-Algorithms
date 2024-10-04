class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r not in range(rows)
            or c not in range(cols)
            or grid[r][c] == 0
            or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            sum = 1
            for dr, dc in directions:
                sum += dfs(r + dr, c + dc)
            return sum

            
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r, c))
        return area
