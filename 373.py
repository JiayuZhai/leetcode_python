class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        :ref:https://blog.csdn.net/qq508618087/article/details/51864835
        """
        l1 = len(nums1)
        l2 = len(nums2)
        cnt = min(k,l1*l2)
        index = [0 for _ in range(l1)]
        ans = []
        while cnt>0:
            cnt-=1
            temMin = float('inf')
            m = 0
            for i in range(l1):
                if index[i] <l2 and nums1[i]+nums2[index[i]]<temMin:
                    temMin = nums1[i]+nums2[index[i]]
                    m = i
            ans.append([nums1[m],nums2[index[m]]])
            index[m]+=1
        return ans
            
            
            
