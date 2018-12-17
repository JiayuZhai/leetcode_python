class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/82824685
        """
        return max(max(A) - min(A) - 2 * K, 0)
