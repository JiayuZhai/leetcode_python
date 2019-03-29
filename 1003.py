class Solution:
    def isValid(self, S: str) -> bool:
        while S.find('abc')!=-1:
            tmp = S.find('abc')
            S= S[:tmp]+S[tmp+3:]
        return len(S)==0
