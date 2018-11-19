class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/79463006
        """
        stack = [] 
        res = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            else:
                stack.append(i)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
        return res
