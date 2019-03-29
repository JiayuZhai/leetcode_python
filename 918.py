class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxv = A[0]
        minv = A[0]
        maxSofar = A[0]
        minSofar = A[0]
        s = A[0]
        for i in range(1,len(A)):
            s+=A[i]
            maxSofar = max(A[i],maxSofar+A[i])
            minSofar = min(A[i],minSofar+A[i])
            maxv = max(maxv,maxSofar)
            minv = min(minv,minSofar)
        if maxv<0:
            return maxv
        return max(maxv,s-minv)
