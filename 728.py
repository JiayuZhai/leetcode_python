class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            flag = True
            tmp = i
            while tmp > 0:
                num = tmp % 10
                tmp //= 10
                if not num or i % num:
                    flag = False
                    break
                
            if flag:        
                res.append(i)
                
        return res
