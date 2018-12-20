class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/82919096
        """
        n = len(row)
        cnt = n // 2
        self.par = [i for i in range(n)]
        for i in range(0, n, 2):
            x = self.find(row[i] // 2)
            y = self.find(row[i + 1] // 2)
            if x != y:
                self.par[x] = y
                cnt -= 1
        return n // 2 - cnt
        
    def find(self, x):
        return x if self.par[x] == x else self.find(self.par[x])
