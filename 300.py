class Solution(object):
    def binary_search(self,num):
        start = 0
        end = len(self.LIS) - 1

        if self.LIS[0] >= num:
            return 0

        while end>start+1:
            middle = (start+end)//2
            if self.LIS[middle] > num:
                end = middle
            elif self.LIS[middle] < num:
                start = middle
            else:
                return middle

        return end


    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0


        self.LIS = [nums[0]]

        for i in range(1,len(nums)):
            num = nums[i]

            if num > self.LIS[-1]:
                self.LIS.append(num)
            else:
                index = self.binary_search(num)

                self.LIS[index] = num
        return len(self.LIS)
