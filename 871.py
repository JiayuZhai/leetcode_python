import heapq
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        :ref:https://blog.csdn.net/wlhwaii/article/details/81142018
        """
        ca = []
        stops, cursor, distance = 0,0,startFuel
        while distance < target:
            while cursor <len(stations) and stations[cursor][0]<=distance:
                
                heapq.heappush(ca, -stations[cursor][1])
                cursor+=1
            if len(ca) ==0:
                return -1
            
            distance+= (-heapq.heappop(ca))
            stops+=1
        return stops
