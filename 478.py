class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        nr = math.sqrt(random.random()) * self.r
        alpha = random.random() * 2 * 3.141592653
        newx = self.x + nr * math.cos(alpha)
        newy = self.y + nr * math.sin(alpha)
        return [newx, newy]
    
#先取x再计算y的边界不是均匀取样，圆心附近要更密集。角坐标取样更均匀


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
