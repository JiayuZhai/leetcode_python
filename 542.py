class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        res = [[0 if j ==0 else 10000 for j in i] for i in matrix]
        def func(i,j):
            res = []
            if i-1>=0:
                res.append([i-1,j])
            if j-1>=0:
                res.append([i,j-1])
            if i+1<m:
                res.append([i+1,j])
            if j+1<n:
                res.append([i,j+1])
            return res
        flag=True
        while flag:
            flag=False
            for i in range(m):
                for j in range(n):
                    if matrix[i][j]!=0:
                        tmp = res[i][j]
                        nb = func(i,j)
                        res[i][j] = min([res[a][b] for a,b in nb])+1
                        if res[i][j] != tmp:
                            flag=True

        return res
