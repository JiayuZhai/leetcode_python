class Solution:
    def hIndex(self, citations: List[int]) -> int:
        nums = sorted(citations, reverse=True)
        i = 0
        while i < len(nums) and nums[i] >= i + 1:
            i += 1
        return i
