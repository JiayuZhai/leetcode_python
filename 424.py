class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        :ref:https://blog.csdn.net/weixin_37373020/article/details/80995986
        """
        tmpMax ,  wins , l, result  =  0, 0, len( s  ), 0 
        d  = [  0  ]  * 26 
        for i in range( l  )  :
            key = ord( s[i] )  - 65 
            d[ key  ] += 1
            tmpMax = max(  tmpMax, d[key]  )
            #控制窗口
            while  i + 1 - wins   - tmpMax  > k :
                xkey =  ord( s[wins]  ) - 65
                d[ xkey ] -= 1
                wins += 1
            result = max( result , i -  wins + 1 )
        return result 

