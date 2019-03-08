# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.end)
        len_interval = len(intervals)
        result,pre=1,0
        for i in range(1,len_interval):
            if intervals[i].start-intervals[pre].end>=0:
                result+=1
                pre=i
        return len_interval-result
