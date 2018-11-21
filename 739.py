class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0 for _ in temperatures]
        for j,t in enumerate(temperatures):
            while len(stack)!=0 and t>temperatures[stack[-1]]:
                res[stack[-1]] = j-stack[-1]
                stack.pop()
            stack.append(j)
        return res
