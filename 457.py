class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        parent = dict((i, i) for i in range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        for i, v in enumerate(nums):
            j = (i + v) % n
            if i != j and nums[j]*nums[i] > 0:
                ri, rj = find(i), find(j)
                if ri == rj:
                    return True
                parent[ri] = rj
        return False
