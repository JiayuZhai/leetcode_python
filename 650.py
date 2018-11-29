class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/79574774
        """
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n /= i
        return res
