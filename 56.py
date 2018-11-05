# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda i: i.start)
        res = []
        for i in intervals:
            if len(res)==0:
                res.append(i)
                continue
            if i.start<=res[-1].end and i.end>res[-1].end:
                j = res.pop()
                res.append(Interval(s=j.start,e=i.end))
            if i.start>res[-1].end:
                res.append(i)
        return res
            
