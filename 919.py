# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """   
        self.root=root
        self.num = self.getNum(root)
        self.dic={'0':'left','1':'right'}
    def getNum(self,nd):
        if nd is None:return 0
        return 1+self.getNum(nd.left)+self.getNum(nd.right)
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        if self.root is None:
            self.root = TreeNode(v)
            self.num=1
            return 0
        
        self.num+=1
        s= bin(self.num)[3:]
        cur = self.root
        for i in s[:-1]:
            cur = getattr(cur,self.dic[i])
        setattr(cur,self.dic[s[-1]],TreeNode(v))
        return cur.val
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
