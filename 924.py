class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        self.data = [i for i in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                if graph[i][j]==1:
                    self.union(i,j)
        rev = {}
        for i in range(n):
            j = self.find(i)
            if j in rev:
                rev[j].add(i)
            else:rev[j]={i}
        onemore = set()
        idx=-1
        for i in initial:
            j = self.find(i)
            if j in onemore:
                if j==self.find(idx):idx=-1
            else:
                onemore.add(j)
                k = self.find(idx)
                if idx==-1 or (len(rev[k]),i)<(len(rev[j]),idx):
                    idx = i
        if idx==-1:return min(initial)
        return idx
        
    def find(self,i):
        if self.data[i]!=i:
            self.data[i] = self.find(self.data[i])
        return self.data[i]
    def union(self,i,j):
        if i!=j:
            n = self.find(i)
            m = self.find(j)
            if n!=m:
                self.data[m] = n
