# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathForm(self, root, val):
        if root == None:
            return 0
        return (1 if root.val == val else 0) +self.pathForm(root.left, val - root.val) + self.pathForm(root.right, val - root.val)
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return self.pathForm(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
