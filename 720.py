class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordSet = set(words)
 
        result = ''
        for word in wordSet:
            if len(word)>len(result) or len(word) == len(result) and word<result:
                if all(word[:k] in wordSet for k in range(1,len(word))) :
                    result = word
 
        return result
