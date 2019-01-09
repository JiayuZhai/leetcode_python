class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs=set(s)
        k=0
        res=0
        for x in strs:
            num=s.count(x)
            if num%2==0:
                res+=num
            else:
                k=1
                res+=num-1
        return k+res
