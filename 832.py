class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        for i in range(m):
            for j in range(m//2):
                A[i][j],A[i][m-1-j] = A[i][m-1-j],A[i][j]
        for i in range(m):
            for j in range(m):
                A[i][j] = 0 if A[i][j]==1 else 1
        return A
