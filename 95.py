# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        x = [i for i in range(1,n+1)]
        def func(s):
            if len(s)==0:
                return [None]
            if len(s)==1:
                return [TreeNode(s[0])]
            else:
                res = []
                for i,n in enumerate(s):
                    left = func(s[:i])
                    right = func(s[i+1:])
                    for l in left:
                        for r in right:
                            node = TreeNode(n)
                            node.left = l
                            node.right = r
                            res.append(node)
                return res
        return func(x)
        
                    
