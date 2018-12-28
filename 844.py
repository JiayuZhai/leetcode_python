class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        newS = ''
        for c in S:
            newS = newS+c if c!='#' else newS[:-1]
        newT = ''
        for c in T:
            newT = newT+c if c!='#' else newT[:-1]
        return newS==newT
        
