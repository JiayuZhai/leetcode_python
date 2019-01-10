# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        if not root:
            return l
        q = []
        q.append(root)
        m = 0
        while len(q)!=0:
            size = len(q)
            m = q[0].val
            while size>0:
                tem = q.pop(0)
                if tem.val>m: m = tem.val
                if tem.left!=None: q.append(tem.left)
                if tem.right!=None: q.append(tem.right)    
                size-=1
            l.append(m)
        return l
