class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total, n = sum(nums),len(nums)
        if total %4 !=0 or n <4:
            return False
        target = total/4
        nums.sort(reverse= True)
        used = [False] * n
        
        def dfs(i,tar):
            if i>= n:
                return tar%target ==0
            if used[i]:
                return dfs(i+1,tar)
            used[i] = True
            
            if nums[i] == tar:
                return True
            if nums[i] < tar:
                tar -=nums[i]
                not_used = [j for j in range(i+1,n) if not used[j]]
                for x in not_used:
                    if dfs(x,tar):
                        return True
            used[i] = False
            return False
        for i in range(n):
            if not dfs(i,target):
                return False
        return True
        
        
