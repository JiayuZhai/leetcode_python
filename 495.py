class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        wakeup, sleep =  0, 0 
    
        prevtime = 0
        for time in timeSeries:            
            if time >= wakeup:
                sleep += duration
            else:
                sleep += (time - prevtime)
            wakeup = time + duration
            prevtime = time        
        return sleep
