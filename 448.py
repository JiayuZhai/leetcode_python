class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        if not len(nums):
            return nums
        for x in nums:
            if nums[abs(x)-1]:
                nums[abs(x)-1] = -abs(nums[abs(x)-1])
        for y in range(0,len(nums)):
            if nums[y] > 0:
                out.append(y+1)
        return out
