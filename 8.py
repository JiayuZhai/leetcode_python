class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        :ref:https://blog.csdn.net/weixin_42304045/article/details/80487218
        """
        import re
        res = re.findall(r"^[\+\-]?\d+",str.strip())
        print(res)
        if res !=[]:
            if int(res[0]) > (2**31-1):
                return (2**31-1)
            if int(res[0]) < (-2**31):
                return (-2**31)
            return int(res[0])
        else:
            return 0
