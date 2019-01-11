class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start, end = 1, len(citations)
        while start <= end:
            h = int((start+end)/2)
            if citations[len(citations)-h] < h: # h应该更小
                end = h-1
            elif len(citations)-h-1>=0 and citations[len(citations)-h-1] > h: # h应该更大
                start = h+1
            else:
                return h
        return 0
            
