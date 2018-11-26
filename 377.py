class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :ref:https://blog.csdn.net/corpsepiges/article/details/52022445
        """
        nums.sort()
        ans = [0 for i in range(target+1)]
        
        for i in range(1,len(ans)):
            for j in range(len(nums)):
                if nums[j]<i:
                    ans[i]+= ans[i-nums[j]]
                else:
                    ans[i]+=i//nums[j]
                    break
        return ans[target]
