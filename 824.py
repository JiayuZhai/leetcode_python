class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        c = 1
        l = []
        for word in words:
            if word[0] in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']:
                word = word+'ma'
            else:
                word = word[1:]+word[0]+'ma'
            l.append(word+'a'*c)
            c+=1
        return ' '.join(l)
