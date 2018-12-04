class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        :ref:https://blog.csdn.net/cloudox_/article/details/70224397
        """
        cur = 1
        res = []
        for i in range(1,n+1):
            res.append(cur)
            if cur *10 <=n:
                cur = cur*10
            elif cur%10 !=9 and cur +1<=n:
                cur+=1
            else:
                while cur//10%10 == 9:
                    cur = cur//10
                cur=cur//10+1
        return res
            
