class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [0 for _ in range(n)]
        num[0] = 1
        index2 = 0
        index3 = 0
        index5 = 0
        result = [0 for _ in range(n)]
        result[0] = 1
        
        begin = 1
        while begin<n:
            result[begin] = min(result[index2]*2,result[index3]*3,result[index5]*5)
            if result[begin] == result[index2]*2 :
                index2+=1
            if result[begin] == result[index3]*3 :
                index3+=1
            if result[begin] == result[index5]*5 :
                index5+=1
            begin+=1
        return result[-1]
