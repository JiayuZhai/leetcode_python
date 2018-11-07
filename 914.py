import math
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck)<2:
            return False
        d= {}
        for n in deck:
            if n not in d:
                d[n] = 0
            d[n]+=1
        m = 0
        for k in d:
            if m <d[k]:
                m = d[k]
        for i in range(2,m+1):
            Flag = True
            for k in d:
                if d[k]%i !=0:
                    Flag=False
                    break
            if Flag:
                return True
        return False
