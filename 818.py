import math
class Solution:
    def __init__(self):
        self.dp = [0 for _ in range(10001)]
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        :ref:https://blog.csdn.net/magicbean2/article/details/80333734
        """
        if self.dp[target]>0:
            return self.dp[target]
        n = int(math.log(target,2))+1
        if 1<<n == target +1:
            self.dp[target] = n
        else:
            self.dp[target] = self.racecar((1<<n)-target-1)+n+1
            for m in range(n-1):
                self.dp[target] = min(self.dp[target], self.racecar(target - (1 << (n - 1)) + (1 << m)) + n + m + 1)
        return self.dp[target]

                                 
