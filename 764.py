from bisect import bisect_left
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        :ref:264ms ans
        """
        rows = [[-1, N] for _ in range(N)]
        cols = [[-1, N] for _ in range(N)]
        for r, c in mines:
            rows[r].append(c)
            cols[c].append(r)
        for i in range(N):
            rows[i].sort()
            cols[i].sort()
        print(rows,cols)
        mxp = 0
        for r in range(N):
            for i in range(len(rows[r])-1):
                left_b = rows[r][i]
                right_b = rows[r][i+1]
                for c in range(left_b+mxp+1, right_b-mxp):
                    idx = bisect_left(cols[c], r) -1
                    up_b = cols[c][idx]
                    down_b = cols[c][idx+1]
                    mxp = max(mxp,min(c-left_b, right_b-c, r-up_b, down_b-r))
        return mxp
