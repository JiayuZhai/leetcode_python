# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def func(root,val):
            if root:
                return root.val == val and func(root.left,val) and func(root.right,val)
            else:
                return True
        return func(root,root.val)
