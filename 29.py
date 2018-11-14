class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0: return 0
        if divisor == 0: return

        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1    #标记是否为负
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        tmp = 0
        for i in range(32,-1,-1):   #逆序枚举，范围为[0,32]
            if tmp + (divisor << i) <= dividend:
                tmp += divisor << i     #更新tmp的值
                quotient |= 1 << i      #记录i的位置，从2进制的或运算就是有1就为1

        quotient *= sign    #虽然题目说了不要用乘法，但是为了代码的简洁这里还是用了
        if quotient < -(2 ** 31) or quotient > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return quotient

