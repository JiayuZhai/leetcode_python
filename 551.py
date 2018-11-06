class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return False if s.count("A") > 1 or "LLL" in s else True
                
