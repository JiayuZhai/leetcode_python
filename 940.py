class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        :ref:https://blog.csdn.net/qq_17550379/article/details/84105392
        """
        end = [0] * 26
        for c in S:
            end[ord(c) - 97] = sum(end) + 1
        return sum(end) % (10**9 + 7)
