class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j =  0,len(s)-1
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
                continue
            l,r = s[i+1:j+1],s[i:j]
            return (l == l[::-1]) or (r == r[::-1])
        return True
