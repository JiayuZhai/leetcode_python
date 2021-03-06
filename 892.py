class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/82083893
        """
        area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]: area += grid[i][j] * 4 + 2
                if i: area -= min(grid[i][j], grid[i-1][j]) * 2
                if j: area -= min(grid[i][j], grid[i][j-1]) * 2
        return area
                    

