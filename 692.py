class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for w in words:
            if d.get(w):
                d[w]+=1
            else:
                d[w] = 1
        tosort = []
        for key in d:
            tosort.append([d[key],key])
        tosort.sort(key=lambda x: (-x[0],x[1]))
        res = []
        for item in tosort:
            if k >0:
                res.append(item[1])
                k-=1
            else:break
        return res
