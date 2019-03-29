class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        lmaxv = A[0]
        maxv = A[0]
        l = 0
        for i in range(len(A)):
            if A[i] < lmaxv:
                lmaxv = maxv
                l = i
            elif A[i] > maxv:
                maxv = A[i]
        return l + 1
