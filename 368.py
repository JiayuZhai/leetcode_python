class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        pre = [-1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j

        max_index = dp.index(max(dp))
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = pre[max_index]
        return res
