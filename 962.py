class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        li = sorted(range(n),key=lambda i: A[i])
        last = n
        mx = 0
        for i in li:
            if i<last:
                last = i
            else:
                mx = max(mx,i-last)
        return mx
