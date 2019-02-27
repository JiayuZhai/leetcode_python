class Solution:
    def maximumSwap(self, num: int) -> int:
        num1=list(str(num))
        #print(num1)
        for i in range(0,len(num1)-1):
            if num1[i]<max(num1[i+1:]):
                max_int=max(num1[i+1:])
                for j in range (len(num1)-1,i,-1):
                    if num1[j]==max_int:
                        num1[i],num1[j]= num1[j],num1[i]
                        #print(num1[i],index_int,max_int)
                        return int("".join(num1))

        return num
