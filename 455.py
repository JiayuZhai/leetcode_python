class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        k = 0
        r = 0
        while i < len(s):
            while k < len(g):
                if s[i] >= g[k]:
                    r += 1
                    if k == len(g) - 1:
                        return r
                    i += 1
                    k += 1
                    break
                else:
                    if i == len(s) - 1:
                        i += 1
                        break
                    else:
                        i += 1
        return r
