class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.count=1
        self.max=0
        self.aa=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
 
        def search(grid,i,j):
            self.aa[i][j]=1
            if i>=1 :
                if grid[i-1][j]==1 and self.aa[i-1][j]==0:
                    self.count = self.count + 1
                    search(grid,i-1,j)
 
            if j>=1 :
                if grid[i][j-1]==1 and self.aa[i][j-1]==0:
                    self.count = self.count + 1
                    search(grid,i,j-1)
            if i<=len(grid)-2 :
                if grid[i+1][j]==1 and self.aa[i+1][j]==0:
                    self.count = self.count + 1
                    search(grid,i+1,j)
            if j<=len(grid[0])-2 :
                if grid[i][j+1]==1 and self.aa[i][j+1]==0:
                    self.count = self.count + 1
                    search(grid,i,j+1)
            if self.count>self.max:
                self.max=self.count
 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.count=1
                if grid[i][j]==1:
                    search(grid,i,j)
 
        return self.max
