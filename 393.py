class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        c = 0
        for n in data:
            print(c)
            if c ==0:
                if n >> 5 == 6:
                    c = 1
                elif n >> 4 == 14:
                    c = 2
                elif n >> 3 == 30:
                    c = 3
                elif n >> 7 != 0:
                    return False
            else:
                if n >> 6 != 2:
                    return False
                c-=1
        return c==0
    
