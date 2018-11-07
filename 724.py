class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        tmp = 0
        for i,n in enumerate(nums):
            if tmp == (s-n)/2:
                return i
            tmp+= n
        return -1
            
