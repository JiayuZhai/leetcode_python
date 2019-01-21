class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        arr = [0 for _ in range(rowIndex+1)]
        arr[0] = 1
        for i in range(1,rowIndex+1):
            arr[i] = arr[i-1] * (rowIndex-i+1) // i
        return arr
