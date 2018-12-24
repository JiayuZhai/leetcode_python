class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        block_num = 1       # To count how many blocks there are
        # To record each coordinate blongs to which block 
        blocks = [[0 for j in range(n)] for i in range(n)]     
        block_map = {}      # To record a block contains which coordinates
        
        # To get which block the point blongs to
        def getBlockNum(i, j):
            if i<0 or j<0 or i==n or j==n: 
                return 0
            else: 
                return blocks[i][j]
        
        def setBlockNum(i, j, k):
            blocks[i][j] = k
            block_map[k][0] += 1
            block_map[k][1].append([i,j])

        # To combine two blocks by setting all points in block k to block l
        def combine2Blocks(l, k):
            coords = block_map[k][1]
            for coord in coords: 
                setBlockNum(coord[0], coord[1], l)
            del block_map[k]
        
        # To calculate blocks and its ordinates
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    ub = getBlockNum(i-1, j)
                    lb = getBlockNum(i, j-1)
                    if ub == 0 and lb ==0: 
                        block_map[block_num] = [0, []]
                        setBlockNum(i, j, block_num)
                        block_num += 1
                    elif ub != 0 and lb != 0:
                        if ub != lb: 
                            combine2Blocks(ub, lb)
                        setBlockNum(i, j, ub)
                    else:
                        setBlockNum(i, j, ub+lb)
                else:
                    blocks[i][j] = 0
        
        # Now, let's count island around a coordinate
        max_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    blks = set([getBlockNum(i-1,j), getBlockNum(i+1,j), 
                               getBlockNum(i,j-1), getBlockNum(i,j+1)])
                    blks.discard(0)
                    areas = 1
                    for blk in blks:
                        areas += block_map[blk][0]
                    if areas > max_island:
                        max_island = areas
                else:
                    if block_map[getBlockNum(i,j)][0] > max_island:
                        max_island = block_map[getBlockNum(i,j)][0]
                    
        return max_island
