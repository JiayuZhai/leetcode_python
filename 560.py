class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = {}
        m[0] = 1
        s,res = 0,0
        for n in nums:
            s += n
            if m.get(s-k):
                res += m[s-k]
            if not m.get(s):
                m[s] = 0
            m[s] +=1
        return res
