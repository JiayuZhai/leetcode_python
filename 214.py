class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        :ref:https://blog.csdn.net/tingting256/article/details/50454924
        """
        r_s = s[::-1]
        ss = s+'#'+r_s
        l1 = len(s)
        l2 = len(ss)
        table = [0 for _ in range(l2)]
        for i in range(1,l2):
            k = table[i-1]
            while k>0 and ss[k]!=ss[i]:
                k = table[k-1]
            if ss[i] == ss[k]:
                k+=1
            table[i] = k
        return s[table[-1]:][::-1]+s
