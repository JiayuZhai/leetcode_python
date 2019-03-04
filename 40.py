class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def find(candidates, target, l):
            if target in candidates:
                res.append(l + [target])
            if target > candidates[0]:
                for i in range(len(candidates) - 1):
                    if i > 0 and candidates[i] == candidates[i - 1]:
                        continue
                    find(candidates[i+1:], target-candidates[i], l+[candidates[i]])

        find(candidates, target, [])
        return res
