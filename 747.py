class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for n in nums:
            if m!=n and n!=0 and m/n<2:
                return -1
        return nums.index(m)
