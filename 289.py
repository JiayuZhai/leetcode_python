class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return None
        else:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    self.checkLife(i,j,board)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] % 2 ==1:
                        board[i][j]=1
                    else:
                        board[i][j]=0

    def checkLife(self,i,j,board):   #检查当前位置细胞的死活。
        m= len(board)
        n= len(board[0])
        dx= [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        count = 0
        #主要是判断边界问题
        if board[i][j]==1 or board[i][j]==2 :  #当前状态是活细胞
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x>=0 and x<m and y>=0 and y<n:  #不出界
                    if board[x][y]==1 or board[x][y]==2: #该状态是活细胞
                        count += 1
            if count > 3 or count < 2:  #下个状态死亡
                board[i][j] = 2
            else:
                board[i][j] = 1

        elif board[i][j]==0 or board[i][j]==3:  #当前状态是死细胞
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x>=0 and x<m and y>=0 and y<n:  #不出界
                    if board[x][y]==1 or board[x][y]==2: #该状态是活细胞
                        count += 1
            if count == 3:  #下个状态 活
                board[i][j] = 3
            else:
                board[i][j] = 0
