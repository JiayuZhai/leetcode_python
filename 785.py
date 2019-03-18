class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph or (not graph[0] and len(graph)==1):
            return True
        d = collections.defaultdict(int)
        # 独立子集分别为 0 1
        deque = collections.deque([])
        for i in range(len(graph)):
            if graph[i]:
                if i not in d:
                    d[i] = 0
                    deque.append((i, 0))
                while deque:
                    node, n = deque.popleft()
                    for no in graph[node]:
                        if no not in d:
                            d[no] = 1 - n
                            deque.append((no, 1-n))
                        elif d[no] == n:
                            return False
        return True
