"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        l = [root]
        r = []
        pre = None
        while l:
            node = l[-1]
            if node.children == [] or node.children[-1] == pre: 
                #是叶节点或者孩子都访问过了，则出栈
                r.append(node.val)
                pre = l.pop() # = node
            else: #否则把全部孩子逆序压栈
                l.extend(node.children[::-1])
        return r
