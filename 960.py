class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        :ref:https://leetcode.com/problems/delete-columns-to-make-sorted-iii/discuss/205679/C%2B%2BJavaPython-Maximum-Increasing-Subsequence
        """
        m, n = len(A), len(A[0])
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    dp[j] = max(dp[j], dp[i] + 1)
        return n - max(dp)
