class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        :ref:https://blog.csdn.net/u014626513/article/details/81234299
        """
        dp = [[0]* len(s) for _ in range(len(s))]
        return self.robot(s,dp,0,len(s) -1)
    
    def robot(self,s,dp,i,j):
        if s == '':
            return 0
        if i == j:
            return 1
        if i > j:
            return 0
        
        if dp[i][j]:
            
            return dp[i][j]
        
        dp[i][j] = self.robot(s,dp,i+1,j) + 1
        
        for k in range(i+1,j+1):
            if s[k] == s[i]:
                dp[i][j] = min(dp[i][j],self.robot(s,dp,i,k-1) + self.robot(s,dp,k+1,j))
                
        return dp[i][j]
