class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        sum_num = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if j+1 <n and i+1 <m:
                    sum_num[i][j] = grid[i][j]+min(sum_num[i][j+1],sum_num[i+1][j])
                elif j+1 <n:
                    sum_num[i][j] = grid[i][j] + sum_num[i][j+1]
                elif i+1 <m:
                    sum_num[i][j] = grid[i][j] + sum_num[i+1][j]
                else:
                    sum_num[i][j] = grid[i][j]
        return sum_num[0][0]
