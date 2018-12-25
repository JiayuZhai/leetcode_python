class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        :ref:https://blog.csdn.net/magicbean2/article/details/79568849
        """
        intervals.sort(key=lambda x: (x[1],-x[0]))
        ans = 0 
        p1 = -1 
        p2 = -1
        for i in range(len(intervals)):
            if intervals[i][0]<=p1:
                continue
            elif intervals[i][0]>p2:
                ans+=2
                p2 = intervals[i][1]
                p1 = p2-1
            else:
                ans+=1
                p1 = p2
                p2 = intervals[i][1]
        return ans 
