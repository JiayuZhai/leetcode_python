class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s == None or s == '':
            return 0
        temp = int(len(s) / (2*k))
        if len(s) % (2*k) != 0:
            temp += 1
        s = list(s)
        for i in range(0, temp):
            if i == temp - 1:
                if len(s) - (i - 1)*(2*k) <= k:
                    s[i*2*k: ] = s[i*2*k: ][::-1]
                else:
                    s[i*2*k: i*2*k + k] = s[i*2*k: i*2*k + k][::-1]
            else:
                s[i*2*k: i*2*k + k] = s[i*2*k: i*2*k + k][::-1]
        return ''.join(s)
