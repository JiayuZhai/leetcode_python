
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = {} # key 为 children, value 为 parent
        candidates = []

        for f, t in edges:
            if t in parent:
                candidates.append([parent[t], t])
                candidates.append([f, t])
            else:
                parent[t] = f

        def findRoot(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen
        
        root, cycle = findRoot(1)
        if not candidates:
            for f, t in edges:
                if f in cycle and t in cycle:
                    res = [f, t]
            return res

        children = collections.defaultdict(list) # key 为 parent, value 为 children
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])
        
        return candidates[all(seen)]
