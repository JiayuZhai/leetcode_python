class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :ref:https://blog.csdn.net/u010429989/article/details/60962761
        """
        if len(nums) <=1:
            return 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        sum_dict = {0:-1}
        sum = 0
        ans = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in sum_dict:
                ans = max(ans,i-sum_dict[sum])
            else:
                sum_dict[sum] = i
        return ans
