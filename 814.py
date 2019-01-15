# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.shouldRemove(root):return None
        return root
    def shouldRemove(self,nd):
        if nd is None:return True
        l = self.shouldRemove(nd.left)
        r = self.shouldRemove(nd.right)
        if l:nd.left = None
        if r:nd.right = None
        return l and r and nd.val==0
