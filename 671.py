# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = root.val
        stack = [root]
        lst = []
        while stack:
            stack_ = []
            for node in stack:
                if node.val != a:
                    lst.append(node.val)
                else:
                    if node.left:
                        stack_.append(node.left)
                    if node.right:
                        stack_.append(node.right)
            stack = stack_
        return min(lst) if lst else -1
