class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left,right = 0,len(A)

        while left < right:
            mid = int((left+right)//2)

            #print(mid)

            if A[mid]<A[mid+1]:  # 如果是大的话 目标一定是 mid+1
                left = mid+1
            else:
                right = mid    # 如果是小的话 不能说明什么 还可能是目标

        return left
