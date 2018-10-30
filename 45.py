class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :ref: https://baijiahao.baidu.com/s?id=1600610931651930297&wfr=spider&for=pc
        """
        step = 0
        lastpos = 0
        maxpos = 0
        for i in range(len(nums)):
            if i>lastpos:
                lastpos = maxpos
                step+=1
            maxpos = max(maxpos,i+nums[i])
        return step
                
            
            
            
