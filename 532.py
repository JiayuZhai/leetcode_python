class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter  
        if k < 0:
            return 0
        count = Counter(nums)
        result = 0
        for key, value in count.items():
            if k == 0:
                if value > 1:
                    result += 1
            else:
                if key + k in count.keys():
                    result += 1
        return result
