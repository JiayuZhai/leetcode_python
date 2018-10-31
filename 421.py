class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :ref:https://kingsfish.github.io/2017/12/15/Leetcode-421-Maximum-XOR-of-Two-Numbers-in-an-Array/#anothor-better-solution
        """
        ans = mask = 0
        for x in range(32)[::-1]:
            mask += 1 << x
            prefixSet = set([n & mask for n in nums])
            temp = ans | 1 << x
            for prefix in prefixSet:
                if temp ^ prefix in prefixSet:
                    ans = temp
                    break
        return ans
