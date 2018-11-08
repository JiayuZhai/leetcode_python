class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/79457764
        If x+1 rabbits have same color, then we get x+1 rabbits who all answer x. now n rabbits answer x. 
        If n%(x+1)==0, we need n/(x+1) groups of x+1 rabbits. 
        If n%(x+1)!=0, we need n/(x+1) + 1 groups of x+1 rabbits. 
        the number of groups is math.ceil(n/(x+1)) and it equals to (n+i)/(i+1) , which is more elegant.
        """
        count = collections.Counter(answers)
        print(count)
        return sum((count[x] + x) // (x + 1) * (x + 1) for x in count)
