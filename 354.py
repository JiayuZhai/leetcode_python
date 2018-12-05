class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def insert(target):
            left, right = 0, len(result) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if result[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(result):
                result.append(target)
            else:
                result[left] = target
 
        result = []
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        for envelope in envelopes:
            insert(envelope[1])
        return len(result)
