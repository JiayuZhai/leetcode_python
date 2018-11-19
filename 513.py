# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deep = 0
        max_deep = 0
        max_val = root.val
        q = [[root,deep]]
        while len(q)!=0:
            tree,d = q.pop(0)
            if tree.left!=None:
                q.append([tree.left,d+1])
            if tree.right!=None:
                q.append([tree.right,d+1])
            if max_deep<d:
                max_deep = d
                max_val = tree.val
        return max_val
