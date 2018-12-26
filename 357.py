class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        res = 10
        t = 9
        if n>10:
            n = 10
        for i in range(1,n):
            t*=(10-i)
            res+=t
        return res
