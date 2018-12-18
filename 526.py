class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """  
        cache = dict()
        def solve(idx, nums):
            if not nums:
                return 1
            key = idx, tuple(nums)
            if key in cache:
                return cache[key]
            ans = 0
            for i, n in enumerate(nums):
                if idx % n == 0 or n % idx == 0:
                    ans += solve(idx + 1, nums[:i] + nums[i+1:])
                cache[key] = ans
            return ans
        return solve(1, tuple(range(1,N + 1)))
            
