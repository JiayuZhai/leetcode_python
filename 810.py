class Solution:
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=0 
        for num in nums:  
            s^=num
        if s==0:
            return True
        return True if len(nums)%2==0 else False
