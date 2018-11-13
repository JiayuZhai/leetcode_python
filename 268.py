class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :ref:等差数列
        """
        return(int(len(nums)*(len(nums)+1)/2)-sum(nums))
