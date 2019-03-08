class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not p or not s: return []
        
        m = len(s)
        n = len(p)
        if m < n:
            return []
        s1 = [0] * 26
        s2 = [0] * 26
        for i in range(n):
            # p中各字母频度
            s2[ord(p[i]) - 97] += 1
        for i in range(n-1):
            # 定义一个len(p)-1大小的滑动窗口，统计窗口内单词频度
            s1[ord(s[i]) - 97] += 1
        result = []
        for i in range(m - n + 1):
            # 窗口大小+1
            s1[ord(s[i+n-1])- 97] += 1
            if s1 == s2:
                result.append(i)
            # 窗口大小-1(即原始窗口向右滑动一格）
            s1[ord(s[i])- 97] -= 1
        return result
