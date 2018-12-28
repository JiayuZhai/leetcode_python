class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        :ref:https://leetcode.com/problems/freedom-trail/discuss/159154/My-7-lines-Python-DP-solution-beats-100-124-ms
        """
        indexes, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring):
            indexes[c].append(i)
        for i in indexes[key[0]]:
            dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in indexes[c]:
                dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in indexes[pre]) + 1
            pre = c
        return min(dp[i] for i in indexes[key[-1]])
            
