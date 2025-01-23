class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        rows = [tuple(row) for row in grid]
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += rows.count(col)
        return count
