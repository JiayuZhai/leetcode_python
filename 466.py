class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        from bisect import bisect_right
        if n1==0:
            return 0
        l1,l2 = len(s1),len(s2)
        idx = {}
        f = []
        i = j = 0
        L1 = l1*n1
        while i<L1:
            while i<L1 and s1[i%l1]!=s2[j%l2]:
                i += 1
            if i<L1 and (j+1)%l2==0:
                if i%l1 not in idx:
                    idx[i%l1] = len(f)
                    f.append(i)
                else:
                    b = idx[i%l1]
                    a = len(idx)
                    rest = L1-f[b]
                    L = i-f[b]
                    k = bisect_right(f,rest%L+f[b]-1) if rest%L else b
                    # print a,b,rest,L
                    # print idx,f
                    ans = (rest//L)*(a-b)+k
                    return ans//n2
            i += 1
            j += 1
        return len(f)//n2
