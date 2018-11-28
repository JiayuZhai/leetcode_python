class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        :ref:https://blog.csdn.net/lirining/article/details/82012796
        """
        rows=len(matrix)
        cols=len(matrix[0])
        row_zero=False
        col_zero=False
        for i in matrix[0]:
            if i==0:
                row_zero=True
        for j in range(rows):
            if matrix[j][0]==0:
                col_zero=True

        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][col]==0:
                    matrix[row][0]=0
                    matrix[0][col]=0

        for row in range(1,rows):
            if matrix[row][0]==0:
                matrix[row]=[0]*cols

        for col in range(1,cols):
            if matrix[0][col]==0:
                for row in range(1,rows):
                    matrix[row][col]=0

        if row_zero:
            matrix[0]=[0]*cols

        if col_zero:
            for row in range(rows):
                matrix[row][0]=0
