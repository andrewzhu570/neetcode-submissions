class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        i, j = 0, 0
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0":
                    continue
                else:
                    self.travelIsland(grid, i, j, ROWS, COLS)
                    res += 1
        return res


    def travelIsland(self, grid, k, l, ROWS, COLS):
        if k < 0 or l < 0 or k >= ROWS or l >= COLS or grid[k][l] == "0":
            return
        grid[k][l] = "0"
        self.travelIsland(grid, k+1, l, ROWS, COLS)
        self.travelIsland(grid, k-1, l, ROWS, COLS)
        self.travelIsland(grid, k, l+1, ROWS, COLS)
        self.travelIsland(grid, k, l-1, ROWS, COLS)