class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = []
        for row in grid:
            max_row.append(max(row))
        max_col = []
        for j in range(len(grid[0])):
            max_col.append(max([grid[i][j] for i in range(len(grid))]))
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res+=min(max_row[j],max_col[i])-grid[i][j]
        return res
