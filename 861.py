class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in A:
            if i[0] == 0:
                for j,k in enumerate(i):
                    i[j] = 0 if k==1 else 1
        for j in range(len(A[0])):
            sums = sum([A[i][j] for i in range(len(A))])
            if sums < len(A)/2:
                for i in range(len(A)):
                    A[i][j] = 0 if A[i][j]==1 else 1
        res = 0
        for i in A:
            for j,k in enumerate(i):
                res+= k<<(len(A[0])-1 - j )
        return res
