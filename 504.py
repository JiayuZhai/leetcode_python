class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        absNum = abs(num)
        while absNum>0:
            res = str(absNum%7)+res
            absNum = absNum//7
        if num<0:
            res = '-'+res
        return res
