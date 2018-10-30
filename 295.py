import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minl = []
        self.maxl = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        m = self.findMedian()
        if num < m:
            heapq.heappush(self.maxl,num*-1)
        else:
            heapq.heappush(self.minl,num)
        if len(self.maxl) > len(self.minl):
            heapq.heappush(self.minl,heapq.heappop(self.maxl)*-1)
        if len(self.minl) - len(self.maxl) > 1:
            heapq.heappush(self.maxl,heapq.heappop(self.minl)*-1)
        

    def findMedian(self):
        """
        :rtype: float
        """
        # print(self.minl,self.maxl)
        if len(self.minl)==0 and len(self.maxl)==0:
            return 0
        if len(self.minl) == len(self.maxl):
            return (float(self.minl[0]) + float(self.maxl[0]*-1)) / 2.0
        else:
            return float(self.minl[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
