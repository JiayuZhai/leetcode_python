class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s_max = sum(nums[0:k])
        tmp = sum(nums[0:k])
        for i in range(k,len(nums)):
            if s_max < tmp-nums[i-k]+nums[i]:
                s_max = tmp-nums[i-k]+nums[i]
            tmp = tmp-nums[i-k]+nums[i]
        return s_max/k
        
