class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        h = len(matrix)
        if h == 0:
            return 0
        w = len(matrix[0])
        dp = [[0 for i in range(w)] for j in range(h)]
        result = 1 if (sum(int(matrix[0][i]) for i in range(w))>0 or sum(int(matrix[i][0]) for i in range(h))>0) else 0
        dp[0] = [int(x) for x in matrix[0]]
        for i in range(1, h):
            dp[i][0] = int(matrix[i][0])     
        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                    result = max(dp[i][j], result)   
        return result**2
