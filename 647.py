class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/79433960
        """
        count = 0
        for i in range(len(s)):
            count += 1
            #回文长度是奇数的情况
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            #回文长度是偶数的情况
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
