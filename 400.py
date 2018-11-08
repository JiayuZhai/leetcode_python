class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        :ref:https://blog.csdn.net/Aurora_ym/article/details/81904133
        """
        #第一步确定n是在几位数里，第二步是确定在几位数的第几位数字的第几位
        #第一步
        digit=1#位数
        while n>digit*9*10**(digit-1):
            n-=digit*9*10**(digit-1)#减去该位数的数字数目再算下一位
            digit+=1
        #第二步，这时的n已经是从这个几位数的开头开始的n了
        a=(n-1)//digit#得到几位数的第几位数字，序号从0开始，所以是（n-1）
        b=(n-1)%digit#得到几位数的第几位数字的第几位
        num=10**(digit-1)+a#得到第几位数字是多少
        res=list(str(num))[b]#数字转字符再转列表把第几位数的第几位切出来
        return int(res)#列表转字符再转数字
