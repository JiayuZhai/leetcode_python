# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        que = [root]
        res = []
        while que:
            res_t = []
            for _ in range(len(que)):
                temp = que.pop(0)
                res_t.append(temp.val)
                if temp.left != None:
                    que.append(temp.left)
                if temp.right !=None:
                    que.append(temp.right)
            res.append(res_t)
        return res
