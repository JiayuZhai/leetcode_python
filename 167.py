class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/82014687
        """
        s = {}
        r = []
        for i in range(len(numbers)):
            if numbers[i] in s.keys():
                r.append(s[numbers[i]]+1)
                r.append(i+1)
                return r
            s[target-numbers[i]] = i
        return None
                
            
