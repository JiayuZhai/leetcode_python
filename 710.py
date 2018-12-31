class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        :ref:https://blog.csdn.net/dpengwang/article/details/83044688
        """
        self.map = {}

        for i in blacklist:
            self.map[i] = 1
        self.M = N - len(blacklist)
        for i in blacklist:
            if i < self.M:
                N = N-1
                while N in self.map:
                    N -= 1
                self.map[i] = N

        # print(self.map)
        # print(self.M)

    def pick(self):
        """
        :rtype: int
        """
        import  random
        res =random.randint(0,self.M-1)
        return self.map[res] if res in self.map else res


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
