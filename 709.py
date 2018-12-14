class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join((chr(ord(s) + 32) if 'A' <= s <= 'Z' else s for s in str))
