class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        start = nums[0]
        current = nums[0]
        res = []
        for i in range(1,len(nums)):
            if nums[i] == current+1:
                current = nums[i]
            else:
                if start == current:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(current))
                start = nums[i]
                current = nums[i]
        if start == current:
            res.append(str(start))
        else:
            res.append(str(start)+'->'+str(current))
        return res
