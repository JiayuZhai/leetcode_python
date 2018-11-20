class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = e = -1
        snums = sorted(nums)
        for i in range(len(nums)):
            if snums[i] != nums[i]:
                if s == -1:
                    s = i
                e = i
        return e-s+1 if e != s else 0
