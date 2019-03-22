class Solution:
    def checkRecord(self, n: int) -> int:
        if n==0:
            return 1
        P, AP,L,LL,AL,ALL,A = 1,0,1,0,0,0,1
        M = 10**9+7
        for i in range(2,n+1):
            P,AP,L,LL,AL,ALL,A = ((P+L+LL)%M, (AP+AL+ALL+A)%M,
                                 P,L,(AP+A)%M,AL,(P+L+LL)%M)
        return (P+AP+L+LL+AL+ALL+A)%M
