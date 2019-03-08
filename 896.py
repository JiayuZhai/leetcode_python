class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        sortA = sorted(A)
        return (A == sortA or list(reversed(A)) == sortA)
            
