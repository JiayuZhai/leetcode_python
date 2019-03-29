class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res=[]
        s=''
        for temp in A:
            s+=str(temp)
        a=int(s)
        b=a+K
        c=str(b)
        for i in range(len(c)):
            res.append(int(c[i]))
        return res
