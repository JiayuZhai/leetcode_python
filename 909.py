class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)

        def get(s):  # 通过编号，获取地图的下标索引
            quot, rem = divmod(s-1, N)  # 求商：quot = a // b, 求余数： rem = a % b
            row = N - 1 - quot  # 因为是左下角开始，所以是减去
            col = rem if row%2 != N%2 else N - 1 - rem  # 确定列
            return row, col

        dist = {1: 0}  # 用于记录
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()  # 出队

            if s == N*N:
                return dist[s]

            for s2 in range(s+1, min(s+6, N*N) + 1):  # 向下扩展子节点，判断入队
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)  # 入队
        return -1
