class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
        return dp[1][n]

