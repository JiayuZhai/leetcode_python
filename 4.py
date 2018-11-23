class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1=len(nums1)
        n2=len(nums2)
        if n1==0:
            if n2%2==0:
                return (nums2[n2//2-1]+nums2[n2//2])/2
            else:
                return nums2[(n2-1)//2]
        if n2==0:
            if n1%2==0:
                return (nums1[n1//2-1]+nums1[n1//2])/2
            else:
                return nums1[(n1-1)//2]
        i=0; j=0; cur=[]; k=0
        mid=(n1+n2)//2
        while i<n1 and j<n2 and k<=mid:
            if nums1[i]<nums2[j]:
                #i+=1
                cur.append(nums1[i])
                i+=1
                k+=1
            else:
                cur.append(nums2[j])
                j+=1
                k+=1
        while i<n1 and k<=mid:
            cur.append(nums1[i])
            i+=1
            k+=1
        while j<n2 and k<=mid:
            cur.append(nums2[j])
            j+=1
            k+=1
        if (n1+n2)%2==1:
            return cur[-1]
        else:
            return (cur[-1]+cur[-2])/2
