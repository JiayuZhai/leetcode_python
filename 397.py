class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        import sys
        if n == 1:
            return 0
        if n == 3:
            return 2
        elif n == sys.maxsize:
            return 2+self.integerReplacement((n>>1)+1)
        if n%2 ==0:
            return 1+self.integerReplacement(n>>1)
        else:
            return self.integerReplacement(n+1)+1 if self.func(n) >1 else self.integerReplacement(n-1)+1
    
    def func(self,n):
        shift = 0
        while ((n>>shift) & 1)==1:
            shift+=1
        return shift
