class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        :ref:https://blog.csdn.net/tstsugeg/article/details/69951556
        """
        h = {}
        c = 0
        for i in range(len(wall)):
            s = 0
            for j in range(len(wall[i])-1):
                s+= wall[i][j]
                if not h.get(s):
                    h[s] = 0
                h[s]+=1
        m = 0
        for i in h:
            m = max(m,h[i])
        return len(wall) - m
