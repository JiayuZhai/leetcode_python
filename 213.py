class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :ref:https://blog.csdn.net/ma412410029/article/details/82785871
        """
        def rob_row(nums):
            res = [0]*len(nums)
            res[0] = nums[0]
            res[1] = max(res[0],nums[1])
            for i in range(2,len(nums)):
                res[i] = max(res[i-1],res[i-2]+nums[i])
            return res[-1]
 
        n = len(nums)
        if n == 0: return 0
        if n <= 2: return max(nums)
        return max(rob_row(nums[1:]),rob_row(nums[:-1]))

