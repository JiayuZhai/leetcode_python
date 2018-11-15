class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        n = len(set(pattern))
        for word in words:
            if len(set(word)) != n:
                continue
            fx = dict()
            equal = True
            for i, w in enumerate(word):
                if w in fx:
                    if fx[w] != pattern[i]:
                        equal = False
                        break
                fx[w] = pattern[i]
            if equal:
                ans.append(word)
        return ans
                        
            
