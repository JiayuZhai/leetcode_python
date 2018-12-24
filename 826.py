class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/83104442
        """
        l = [[difficulty[i], profit[i]] for i in range(len(profit))]
        l.sort()
        worker.sort()
        curMax, i = 0, 0
        res = 0
        for w in worker:
            while i<len(profit) and w >=l[i][0]:
                curMax = max(curMax, l[i][1])
                i += 1
            res += curMax
        return res
