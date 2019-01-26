class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        arr = sorted(A,reverse=True)
        ret = []
        n = len(arr)
        for i,mx in enumerate(arr):
            cur = A.index(mx)+1
            ret.append(cur)
            ret.append(n-i)
            A[:cur] = A[:cur][::-1]
            A[:n-i] = A[:n-i][::-1]
        return ret
