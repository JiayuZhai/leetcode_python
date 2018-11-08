class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        :ref:https://blog.csdn.net/qq_38595487/article/details/81411848
        """
        l = [ord(c)-ord('a') for c in list(p)]
        max_l = [0]*26
        m=0
        for i,n in enumerate(l):
            if i>0 and (l[i] - l[i-1] ==1 or (l[i]==0 and l[i-1]==25)):
                m+=1
            else:
                m=1
            max_l[l[i]] = max(m,max_l[l[i]])
        return sum(max_l)
