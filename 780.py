class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        :ref:https://blog.csdn.net/u011026968/article/details/79560140
        """
        while tx > sx and ty > sy :
            if (ty > tx) :
                ty %= tx
            else :
                tx %= ty
            
        
        return (ty==sy or tx!=0 and (ty - sy) % tx == 0 ) and (ty!=0 and (tx - sx) % ty == 0 or sx == tx)
