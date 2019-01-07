class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        value = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1))[::-1]:
            for j in range(len(num2))[::-1]:
                value[i+j+1] += (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
        carry = 0
        for i in range(len(value))[::-1]:
            value[i]+=carry
            carry = value[i]//10
            value[i] %= 10
        beginIndex = 0
        while beginIndex < len(value)-1 and value[beginIndex]==0:
            beginIndex +=1
        for i in range(beginIndex,len(value)):
            value[i] = chr(ord('0')+value[i])
        return ''.join(value[beginIndex:])
