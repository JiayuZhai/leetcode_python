class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<=2:
            return 0
        dp,s = 0,0
        d1= A[1]-A[0]
        for i in range(2,len(A)):
            d2 = A[i] - A[i-1]
            if d2 == d1:
                dp+=1
                s += dp
            else:
                dp=0
            d1 = d2
        return s
