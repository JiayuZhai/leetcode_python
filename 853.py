class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        res = 0
        if position:
            res += 1
        else:
            return res
        
        hashDict = {}
        for nums in range(len(position)):
            hashDict[position[nums]] = speed[nums]
    
        position.sort(reverse=True)
        
        pre = position[0]
        for _next in position[1:]:
            time_pre = (target - pre)/hashDict[pre]
            time_next = (target - _next)/hashDict[_next]
            if time_next<=time_pre:
                continue
            else:
                pre = _next
                res += 1
        return res
