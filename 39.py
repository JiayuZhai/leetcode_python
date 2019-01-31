class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.recursive(candidates, target, 0, [], ret)
        return ret
    def recursive(self, candidates, target, i, pre=[], ret=[]):

        if i == len(candidates):
            return

        st = []
        while target >= candidates[i]:
            target -= candidates[i]
            st.append(candidates[i])

        if target == 0:
            ret.append(pre+st)
        else:
            self.recursive(candidates, target, i + 1, pre+st, ret)

        while st:
            target += st.pop()
            self.recursive(candidates, target, i + 1, pre+st, ret)
