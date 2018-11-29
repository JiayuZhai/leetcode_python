class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = min(nums)-1
        max2 = max1
        max3 = max1
        for n in nums:
            if max1 <n:
                max3 = max2
                max2 = max1
                max1 = n
                
            elif max2 <n and max1 !=n:
                max3 = max2
                max2 = n
            elif max3 <n and max2 !=n and max1 !=n:
                max3 = n
        
        return max3 if max3!= min(nums)-1 else max1
