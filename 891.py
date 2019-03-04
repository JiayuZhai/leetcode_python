class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        s = diff = 0 
        k = 1 << max(len(A)-2,0)
        A.sort() 
        for i in range(len(A)):
            diff += A[~i] - A[i] 
            s += k * diff 
            k >>= 1 
        return s % (10 ** 9 + 7)
