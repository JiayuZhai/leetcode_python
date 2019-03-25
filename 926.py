class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        m = S.count('0')
        res = [m]
        for s in S:
            if s == '1':
                m+=1
            else:
                m-=1
                res.append(m)
        return min(res)
