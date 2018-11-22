class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=set(words)
        #单独定义了一个是否是连接串的函数
        def isconcated(w,c):
            if w in c:
                return c[w]
            n=len(w)
            for i in range(1,n):
                p=w[:i]#遍历判断是否存在可构成的单词
                if p in a:
                    left=w[i:]#判断剩余的部分可否构成连接串
                    if left in a or isconcated(left,c):
                        c[w]=True
                        return True
            c[w]=False
            return False

        c={}#这个字典设置的很精妙，大大减少了运行次数，使得这个程序没有超时的很大原因在于此。
        return [w for w in words if isconcated(w,c)]
