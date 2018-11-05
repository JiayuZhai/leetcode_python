class StockSpanner:

    def __init__(self):
        self.l = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if len(self.l)==0:
            self.l.append([price,1])
            return 1
        if price <self.l[-1][0]:
            self.l.append([price,1])
            return 1
        else:
            res = 1
            while len(self.l)>0 and self.l[-1][0]<=price:
                p,i = self.l.pop()
                res+=i
            self.l.append([price,res])
            return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
