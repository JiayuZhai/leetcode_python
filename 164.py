class Bucket:
    def __init__(self,m=0,M=0,isempty=True):
        self.m = m
        self.M = M
        self.isempty = isempty
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        Buckets = [Bucket() for _ in range(len(nums)+1)]
        max_num = max(nums)
        min_num = min(nums)
        if max_num == min_num:
            return 0
        for num in nums:
            index = int((num-min_num)/(max_num-min_num)*len(nums))
            bucket = Buckets[index]
            if bucket.isempty:
                bucket.m = num
                bucket.M = num
                bucket.isempty = False
            else:
                bucket.m = min(num,bucket.m)
                bucket.M = max(num,bucket.M)
        res = 0
        pre_max = Buckets[0].M
        for i in range(1,len(Buckets)):
            if not Buckets[i].isempty:
                res = max(res,Buckets[i].m - pre_max)
                pre_max = Buckets[i].M
        return res
