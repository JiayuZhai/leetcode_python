class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len(set([self.hash(s) for s in A]))
    
    def hash(self, s):
        return ''.join(sorted(s[::2]) + sorted(s[1::2]))
