class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        from collections import Counter
        count = 0
        words = Counter(words)
        for word,num in words.items():
            start = 0
            flag = False
            for alp in word:
                start = S.find(alp,start) + 1
                if start == 0:
                    flag = True
                    break
            if not flag:
                count += num
        return count
