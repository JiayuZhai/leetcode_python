class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        lvl, c = 0, 1
        while lvl <= n//2:
            if c <= n*n:
                for i in range(lvl, n-lvl):
                    matrix[lvl][i] = c
                    c += 1
            if c <= n*n:
                for i in range(lvl+1, n-lvl):
                    matrix[i][n-lvl-1] = c
                    c += 1
            if c <= n*n:
                for i in range(n-lvl-2, -1+lvl, -1):
                    matrix[n-lvl-1][i] = c
                    c += 1
            if c <= n*n:
                for i in range(n-lvl-2, lvl, -1):
                    matrix[i][lvl] = c
                    c += 1
            lvl += 1

        return matrix
