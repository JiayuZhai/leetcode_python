class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row, col, block = [{} for i in range(9)],[{} for i in range(9)],[{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                term = board[i][j]
                if term != '.':
                    if term not in row[i]:
                        row[i][term] = True
                    else:
                        return False
                    if term not in col[j]:
                        col[j][term] = True
                    else:
                        return False
                    if term not in block[3*(i//3)+(j//3)]:
                        block[3*(i//3)+(j//3)][term]=True
                    else:
                        return False
        return True
            
