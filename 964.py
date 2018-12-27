class Solution:
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        :ref:http://www.mamicode.com/info-detail-2562485.html
        """
        l = []
        while target !=0:
            l.append(target%x)
            target //= x
        self.best = 10000000000
            
        def dfs(l,k,add, count):
            if count >=self.best:
                return
            if add == 0 and k >= len(l):
                self.best = min(self.best, count)
                return

            if k < len(l):
                add += l[k]

            cost = 2 if k == 0 else k
            cur = add % x
            add //= x
            dfs(l, k + 1, add, count + cost * cur)
            if cur != 0 and k<= len(l) + 2:
                dfs(l, k + 1, 1, count + cost * (x - cur))
        
        dfs(l,0,0,0)
        return self.best -1
             
