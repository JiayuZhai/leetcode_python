# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        def func(root):
            if root == None:
                return 0
            x = func(root.left)+ func(root.right) + root.val
            if x not in d:
                d[x] = 0
            d[x] += 1
            return x
        func(root)
        tt = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [tt[i][0] for i in range(len(tt)) if tt[i][1] == tt[0][1]]
        
