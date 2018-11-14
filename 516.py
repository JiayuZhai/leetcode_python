class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == s[::-1]:
            return n
        dp = [0] * n
        dp[n-1] = 1
        for i in range(n-1, -1, -1):
            tmp = dp[:]
            tmp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    tmp[j] = 2 + dp[j-1]
                else:
                    tmp[j] = max(dp[j], tmp[j-1])
            dp = tmp[:]
            print(dp)
        return dp[n-1]
