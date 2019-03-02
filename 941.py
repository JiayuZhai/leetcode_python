class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:
            return False
        i = A.index(max(A))
        return i!=0 and i!=len(A)-1 and sorted(set(A[:i])) == A[:i] and sorted(set(A[i:]))[::-1] == A[i:]
