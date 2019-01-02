# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    #ref:https://blog.csdn.net/hyperbolechi/article/details/43951283
    def cloneGraph(self, node):
        if node==None:
            return node
        que=[node]
        head=UndirectedGraphNode(node.label)
        dict={node:head}
        while que:
            curr=que.pop(0)
            for n in curr.neighbors:
                if n in dict:
                    dict[curr].neighbors.append(dict[n])
                else:
                    que.append(n)
                    copy=UndirectedGraphNode(n.label)
                    dict[n]=copy
                    dict[curr].neighbors.append(copy)
        return head
