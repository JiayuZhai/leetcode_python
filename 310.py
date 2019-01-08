class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        g= {}
        for a,b in edges:
            if a not in g:
                g[a] = set([b])
            else:
                g[a].add(b)
            if b not in g:
                g[b] = set([a])
            else:
                g[b].add(a)
        while len(g)>2:
            li = [i for i in g if len(g[i])==1]
            for i in li:
                x = g.pop(i).pop()
                g[x].remove(i)
        li = list(g.keys())
        if len(li)==0:return [0]
        else: return li
