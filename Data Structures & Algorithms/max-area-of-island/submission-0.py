class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        i, j = 0, 0
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    continue
                else:
                    current = self.travelIsland(grid, i, j, ROWS, COLS)
                    if current > res:
                        res = current
        return res


    def travelIsland(self, grid, k, l, ROWS, COLS):
        if k < 0 or l < 0 or k >= ROWS or l >= COLS or grid[k][l] == 0:
            return 0
        grid[k][l] = 0
        return 1 + self.travelIsland(grid, k+1, l, ROWS, COLS) + self.travelIsland(grid, k-1, l, ROWS, COLS) + self.travelIsland(grid, k, l+1, ROWS, COLS) + self.travelIsland(grid, k, l-1, ROWS, COLS)