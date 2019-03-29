class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        c = collections.Counter(A)
        for cc in c:
            if c[cc] == len(A)//2:
                return cc
            
