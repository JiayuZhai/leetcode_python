class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/82917210
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        cache = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                path = self.dfs(matrix, cache, m, n, i, j)
                res = max(res, path)
        return res
        
    def dfs(self, matrix, cache, m, n, i, j):
        if cache[i][j] != -1:
            return cache[i][j]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 1
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            path = 1 + self.dfs(matrix, cache, m, n, x, y)
            res = max(path, res)
        cache[i][j] = res
        return cache[i][j]

