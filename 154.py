class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l== 1: return nums[0]
        p1,p2,mid =0,l-1,0
        if nums[l-1]>nums[0]: return nums[0]
        while p1<p2:
            mid = (p1+p2)>>1
            if nums[mid]>nums[p2]:
                p1 = mid+1
            elif nums[mid]<nums[p2]:
                p2 = mid
            else:
                p2 = p2-1
        return nums[p1]
                
