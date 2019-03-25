# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def func(root, l):
            if root:
                l.append(root.val)
                func(root.left,l)
                func(root.right,l)
            return l
        return func(root,[])
