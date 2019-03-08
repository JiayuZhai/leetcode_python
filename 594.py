class Solution:
    def findLHS(self, nums: List[int]) -> int:
        r = []
        a = {}
        for i in nums:
            a[i] = a.get(i,0) + 1
        for i in a:
            if i+1 in a:
                r.append(a[i] + a[i+1])
        if r == []:
            return 0
        return max(r)
