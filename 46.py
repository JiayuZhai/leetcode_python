class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) ==1 or len(nums) ==0:
            return [nums]
        res = []
        for i in range(len(nums)):
            p = self.permute(nums[0:i]+nums[i+1:])
            for j in p:
                res.append([nums[i]]+j)
        return res
