class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/81977433
        """
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
