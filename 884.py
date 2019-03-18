class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d = {}
        for w in A.split(' '):
            d[w] = d.get(w,0)+1
        for w in B.split(' '):
            d[w] = d.get(w,0)+1
        res = []
        for w in d:
            if d[w] ==1:
                res.append(w)
        return res
