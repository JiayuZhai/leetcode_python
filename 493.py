class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_and_count(lo, hi):
            if lo == hi:
                return 0

            count = 0
            mid = (lo + hi) // 2
            count += merge_and_count(lo, mid) + merge_and_count(mid + 1, hi)
            left = lo
            right = mid + 1
            while left <= mid and right <= hi:
                if nums[left] > 2 * nums[right]:
                    # 如果我们找到了有效对，则left和mid之间的元素也将是有效对。计算这些元素
                    count += mid - left + 1
                    # 增加右指针以检查左侧元素是否可以与其中任何一个匹配
                    right += 1
                else:
                    left += 1
            # 核心
            nums[lo: hi + 1] = sorted(nums[lo: hi + 1])  # 排序是因为 mid 左右两边在比较的时候可以,节省时间，否则需要 o(n^2)

            return count

        if not nums:
            return 0

        return merge_and_count(0, len(nums) - 1)
