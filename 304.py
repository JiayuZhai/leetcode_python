class NumMatrix:
    # 先用dp把matrix里每个点(i,j)所代表的0~i，0~j的大方块面积算出来
    # 然后sumRegion就只是在做方块面积拼接
    def __init__(self, matrix: List[List[int]]):
        self.mtx = matrix
        if self.mtx:
            self._dp = self._core()
    
    def _core(self):
        dp =[[0]*(len(self.mtx[0])+1) for i in range(len(self.mtx)+1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + self.mtx[i-1][j-1]
        return dp
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        if self.mtx:
            res = self._dp[row2+1][col2+1] - self._dp[row2+1][col1] - self._dp[row1][col2+1] + self._dp[row1][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
