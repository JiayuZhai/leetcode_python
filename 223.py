class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        a1 = (C-A)*(D-B)
        a2 = (G-E)*(H-F)
        
        def func(A,B,C,D,E,F,G,H):
            h1 = max(A,E)
            h2 = min(C,G)
            h = h2-h1
            v1 = max(B, F)
            v2 = min(D, H)
            v = v2 - v1
            if h<=0 or v<=0: return 0
            return h*v
            
        overlap = func(A,B,C,D,E,F,G,H)
        return a1+a2-overlap
        
        
