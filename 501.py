# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.d = {}
        def func(root):
            if root:
                if not self.d.get(root.val):
                    self.d[root.val] = 0
                self.d[root.val]+=1
                func(root.left)
                func(root.right)
        func(root)
        d = sorted(self.d.items(),key = lambda x: x[1], reverse= True)
        m = d[0][1]
        res = []
        for item in d:
            if item[1]==m:
                res.append(item[0])
            else:
                break
        return res
            
