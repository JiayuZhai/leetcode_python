class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def isSame(diff):
            for i in range(len(diff)):
                if diff[i]!=0:
                    return False
            return True
        
        if s1 is None or s2 is None or len(s1)>len(s2):
            return False
        c1 = [0 for _ in range(26)]
        c2 = [0 for _ in range(26)]
        for i in range(len(s1)):
            c1[ord(s1[i])-ord('a')]+=1
            c2[ord(s2[i])-ord('a')]+=1
        diff = []
        for i in range(26):
            diff.append(c2[i] - c1[i])
        for i in range(len(s1),len(s2)):
            if isSame(diff):
                return True
            diff[ord(s2[i-len(s1)]) - ord('a')]-=1
            diff[ord(s2[i])-ord('a')] +=1
        return isSame(diff)
