class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def check(dd,d):
            for c in range(26):
                if d[c]<dd[c]:
                    return False
            return True
        dd = [0]*26
        for b in B:
            d = [0]*26
            for c in b:
                d[ord(c)-ord('a')] +=1
            for i in range(26):
                dd[i] = max(dd[i],d[i])
        res = []
        for a in A:
            d = [0]*26
            for c in a:
                d[ord(c)-ord('a')] +=1
            if check(dd,d):
                res.append(a)
        return res
