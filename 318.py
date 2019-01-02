class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        h = [0 for _ in range(n)]
        m = 0
        for i in range(n):
            for c in words[i]:
                h[i] = 1<<(ord(c)-ord('a')) | h[i]
        
        for i in range(n-1):
            for j in range(i+1,n):
                if h[i]&h[j]==0:
                    m = max(len(words[i])*len(words[j]),m)
        return m
                
