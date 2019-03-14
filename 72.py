class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(s, t):
            k = (s, t)
            if k not in memo:
                if not s or not t:
                    memo[k] = len(s) + len(t)
                elif s[0] == t[0]:
                    memo[k] = helper(s[1:], t[1:])
                elif s[-1] == t[-1]:
                    memo[k] = helper(s[:-1], t[:-1])
                else:
                    memo[k] = 1 + min(helper(s[1:], t[1:]), helper(s[1:], t), helper(s, t[1:]))
            return memo[k]
        return helper(word1, word2)
