class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m = 0
        s = []
        ma = -1
        l = 0
        ans = 0 
        for i in arr:
            if i >= m:
                s.append(i)
                ma = max(ma,i)
                l += 1
                if l == ma + 1 - m:
                    m = ma + 1
                    s = []
                    ma = -1
                    l = 0
                    ans += 1
        return ans
