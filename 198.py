class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums)+2)]
        for i,n in enumerate(nums):
            dp[i] += max(dp[i-1],nums[i]+dp[i-2])
        return dp[len(nums)-1]
