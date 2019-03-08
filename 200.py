class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        row,col=len(grid),len(grid[0])
        visited=[[0 for x in range(0,col)] for y in range(0,row)]
        count=0
        for i in range(0,row):
            for j in range(0,col):
                if visited[i][j]==0 and grid[i][j]=='1':
                    self.dfs(grid,i,j,visited)
                    count=count+1
        return count
    
    def dfs(self,grid,i,j,visited):
        if i<0 or i>=len(grid):
            return
        if j<0 or j>=len(grid[0]):
            return
        if grid[i][j]=='0' or visited[i][j]==1:
            return
        visited[i][j]=1
        self.dfs(grid,i-1,j,visited)
        self.dfs(grid,i+1,j,visited)
        self.dfs(grid,i,j-1,visited)
        self.dfs(grid,i,j+1,visited)
