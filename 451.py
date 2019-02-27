class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        temp = ''
        n = len(s)
        for i in range(0, n):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1

        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        
        for x in sorted_dic:
            temp += x[0] * x[1]
        return temp
