class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        vec = {}
        n = len(points)
        mn = None
        visited=set()
        for i in range(n-1):
            for j in range(i+1,n):
                x1,y1=points[i]
                x2,y2 = points[j]
                dx = x1-x2
                dy = y1-y2
                new = (i,j)
                if dx<0:
                    dx = -dx
                    dy = -dy
                    new = (j,i)
                v = (dx,dy)  # edge  vec
                if v in vec:
                    for p,q in vec[v]: # edge vecs are the same, namely  line ij//pq
                        if p==i or p==j or q==i or q==j:continue
                        xp,yp= points[p]
                        xq,yq=points[q]
                        ip = tuple(sorted([i,j,p,q]))
                        if  ip not in visited:
                            visited.add(ip) # line  ij//pq or  iq//pj,  just judge them once
                            dx2,dy2 = x1-xq, y1-yq
                            if dx*dx2+dy*dy2!=0:  # line ij,line iq are not vertical. line iq may be a diagonal
                                dx2,dy2 = x1-xp,y1-yp
                            if dx*dx2+dy*dy2!=0: # not rectangle, it's Parallelogram
                                continue
                            s = abs(dx*dy2-dy*dx2)
                            if s!=0:  # Three points shouldn't be on one line
                                if  mn is None or mn>s:mn = s
                    vec[v].add(new)
                else:vec[v]={new}
        return 0 if mn is None else float(mn)
