class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        nums = [0 for i in range(121)]#记录各个年龄段有多少人
        sums = [0 for i in range(121)]#记录小于对应年龄段的人数多少
        count = 0
        
        for i in range(len(ages)):
            nums[ages[i]] += 1
            
        for i in range(121):
            sums[i] += sums[i-1] + nums[i]
            
        for i in range(15,121): #由条件1 得到15岁以下不会有friend request
            if nums[i] == 0:
                continue
            j = sums[i] - sums[int(i/2)+ 7]#这个范围中间的人都可以friend request
            j -= 1 #自己不能给自己发
            count += j * nums[i]
            
        return count
