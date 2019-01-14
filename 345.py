class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuanyin = 'aeiouAEIOU'
        l = list(s)
        print(l)
        i = 0
        j = len(s)-1
        while i<j:
            if l[i] not in yuanyin:
                i+=1
                continue
            if l[j] not in yuanyin:
                j-=1
                continue
            if i<j:
                l[i],l[j] = l[j],l[i]
                i+=1
                j-=1
        return ''.join(l)
