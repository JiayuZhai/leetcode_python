class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c = 0
        for ji in J:
            c += S.count(ji)
        return c
