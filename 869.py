class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        l = [list(str(2**i)) for i in range(32)]
        for i in l:
            i.sort()
        s = list(str(N))
        s.sort()
        for i in l:
            if i == s:
                return True
        return False
