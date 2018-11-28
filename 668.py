class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        l = 1
        r = m*n
        while l<=r:
            mid = (l+r)//2
            count = 0
            for i in range(1,m+1):
                j=mid//i
                count += min(j,n)
                if count >= k:
                    r = mid-1
                    break
            if count < k:
                l = mid+1
                
        return l
