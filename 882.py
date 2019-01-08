class Solution:
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        :ref:https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/discuss/210586/python-using-heap
        """
        g = collections.defaultdict(dict)
        for i,j, k in edges:
            g[i][j] = g[j][i] = k + 1
        s = [0] * N
        s[0] = 1
        queue = [(0 , 0)]
        ans = 0
        while queue:
            curr, u = heapq.heappop(queue)
            left = M - curr
            for v in g[u]:
                if left >= g[u][v] > 0:
                    ans += g[u][v]-1
                    s[v] = 1
                    heapq.heappush(queue, (curr + g[u][v], v)) 
                    g[u][v] = g[v][u] = 0 
                elif g[u][v] > 0:
                    ans += left 
                    g[v][u] -= left 
                    g[u][v] = 0
        return ans + sum(s) 
