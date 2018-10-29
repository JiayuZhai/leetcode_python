# -*- coding: utf-8 -*-

'''获取所有钥匙的最短路径'''
from collections import namedtuple,deque

# 定义网格节点
GridNode = namedtuple('GridNode',['i','j','key_state'])

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        :ref: https://blog.csdn.net/u014230646/article/details/81189340
        """
        # 要求最短路径，采用广度优先搜索。用队列实现广度优先搜索。
        # 因为增加了钥匙，所以我们需要引入状态，以表达当前有多少钥匙。在同一个位置，若拥有的钥匙数目不同，则
        # 视为不同的状态，这些状态需要入队;若当前状态此前已经访问过（即钥匙数与坐标位置都相同视为同一个状态），则
        # 可跳过，无需访问。
        # key只有6种，我们用一个int类型保存当前已经拥有的key的情况，只需要6bit。
        # 我们从起点开始搜索，遇到钥匙就更新记录，遇到墙就跳过，遇到門若有钥匙则通过，若没有钥匙则跳过。此外，如果当前
        # 状态已经遍历过，就跳过，否则加入队列，这些属于广度优先搜索的基本操作。
        # 需要注意以下几点。

        keys_lst = ['a','b','c','d','e','f']
        doors_lst = ['A','B','C','D','E','F']

        m = len(grid)
        n = len(grid[0])

        # 包含所有钥匙，用6bit表示
        allkey_state = 0
        # 已经访问过的状态：m*n*64
        status_seen = [[[0 for k in range(64)] for j in range(n)] for i in range(m)]

        # 读取起点和钥匙所在的位置
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start_i = i
                    start_j = j
                if c in keys_lst:
                    allkey_state = allkey_state | (1<< keys_lst.index(c))
        # 队列q，初始节点
        q = deque()
        q.append(GridNode(start_i, start_j, 0))
        # 搜索方向，左右上下
        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        step = 0
        # 我们要找的是找到所有key的最短路径，因此每次我们处理距离最开始的起点距离为step的节点，同时把他们的邻居入队（为下一层的节点，step+1）
        while q:
            # 先把距离最开始的起点step步长的情况下的，待处理的节点都处理完
            nq = len(q)
            while nq:
                nq = nq - 1
                # 队列头部
                node = q.popleft()
                row = node.i 
                col = node.j
                key_state = node.key_state
                # 已找到所有的钥匙
                if key_state == allkey_state:
                    return step
                # 访问节点的所有邻居
                for delta in dirs:
                    row = node.i + delta[0]
                    col = node.j + delta[1]
                    key_state = node.key_state
                    if row < 0 or row >= m or col <0 or col >=n:
                        continue
                    c = grid[row][col]

                    # 遇到墙壁
                    if c == '#':
                        continue
                    # 遇到门且没有钥匙
                    if c in doors_lst:
                        if not (1<<doors_lst.index(c)) & key_state:
                            continue
                    # 遇到钥匙则更新我们的钥匙
                    if c in keys_lst:
                        key_state = key_state | (1<<keys_lst.index(c))
                    # 判断当前的状态是否已经访问过，若否，则加入队列，等下次访问
                    if status_seen[row][col][key_state]:
                        continue
                    q.append(GridNode(row, col, key_state))
                    # 表明已经访问过
                    status_seen[row][col][key_state] = 1
            # 处理下一层的节点
            step = step + 1    
        return -1