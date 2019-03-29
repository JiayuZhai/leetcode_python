class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        pre = collections.defaultdict(int)
        # 不能直接等于1，因为如果nums[0]为0，就会少算
        pre[-nums[0]] += 1
        pre[nums[0]] += 1
        for num in nums[1:]:
            cur = collections.defaultdict(int)
            for vl in pre:
                cur[vl+num] += pre[vl]
                cur[vl-num] += pre[vl]
            pre = cur
        # 注意是用pre，因为如果nums只有一个元素，cur根本没机会定义
        return pre[S]
