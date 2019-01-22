# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.f(root)
        return root
    def f(self,root,n=0):
        if root is None:return n
        if not(root.left or root.right):
            root.val+=n
            return root.val
        rn = self.f(root.right,n)
        root.val +=rn
        ln = self.f(root.left,root.val)
        return ln
