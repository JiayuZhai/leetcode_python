class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<10:
            return []
        m = {'A':0,'C':1,'G':2,'T':3}
        ss = {}
        res = set()
        for i in range(len(s)-9):
            bit = 0
            sub = s[i:i+10]
            for j,c in enumerate(sub):
                bit += m[c]<<(2*j)
            if bit not in ss:
                ss[bit] = True
            else:
                res.add(s[i:i+10])
        return list(res)
                
