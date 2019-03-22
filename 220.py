class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        le=len(nums)
        s=sorted(range(le),key=lambda x:nums[x])
        for i in range(le):
            for j in range(i+1,le):
         
                if abs(s[i]-s[j])<=k:
                    if abs(nums[s[j]]-nums[s[i]])<=t:
                        return True
                    else:
                         break
                
        return False
