class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for s in cpdomains:
            a,b = s.split(' ')
            n = int(a)
            b = b.split('.')
            for i in range(len(b)):
                domain = '.'.join(b[i:])
                d[domain] = d.get(domain,0)+n
        res = []
        for key in d:
            res.append(str(d[key])+ ' ' +key)
        return res
