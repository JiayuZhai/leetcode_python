class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank_margin,start,min_tank_margin = 0,0,float('inf') 
        #油箱余量，开始油站，油箱最小余量（最小余量之后那一个即为开始油站）
        n = len(gas)
        for i in range(n):
            tank_margin += gas[i]-cost[i]
            if tank_margin < min_tank_margin:
                min_tank_margin = tank_margin
                start = (i+1)%n
        if tank_margin < 0:    #如果余量为负，则不能走完
            return -1
        return start
