# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N==1:
            return [TreeNode(0)]
        if N%2 == 0:
            return []
        res = []
        for i in range(1,N,2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res
        
