class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        :ref:https://blog.csdn.net/u014626513/article/details/81227574
        """
        #涉及子串动态规划利用(i,j)进行地推   dp[i][j][k]表示从i到j子串并且右端存在与j相同的k个字符其获得的最大点数。
        n = len(boxes)
        dp = [[[0]*n for _ in range(n)]for _ in range(n)]
        return self.robot(boxes,dp,0,n-1,0)
    
    def robot(self,boxes,dp,x,y,k):
        if x > y:
            return 0
        if dp[x][y][k] > 0:
            return dp[x][y][k]
        while x < y and boxes[y] == boxes[y-1]:
            y -= 1
            k += 1
            
        dp[x][y][k] = self.robot(boxes,dp,x,y-1,0) + (k+1)*(k+1)
        for i in range(x,y):
            if boxes[i] == boxes[y]:
                dp[x][y][k] = max(dp[x][y][k],self.robot(boxes,dp,x,i,k+1) + self.robot(boxes,dp,i+1,y-1,0))
        return dp[x][y][k]

