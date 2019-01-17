class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        b=0
        for i in points:
           # s中保存所有到i距离相同的点的个数，键是距离
            s={}
            for j in points:
                a=(i[0]-j[0])**2+(i[1]-j[1])**2
                if a in s:
                    s[a]+=1
                else:
                    s[a]=1
            for k in s:
                if s[k]>1:
                    b+=s[k]*(s[k]-1)
        return b
