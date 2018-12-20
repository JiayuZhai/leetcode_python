class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        m = n
        while n:
            s +=n%5
            n = n//5
        return (m-s) >>2
