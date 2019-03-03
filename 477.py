class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [0]*31
        for n in nums:
            ct = 0
            while n:
                if n%2==1:bits[ct]+=1
                n>>=1
                ct+=1
        total = len(nums)                
        return sum(i*(total-i) for i in bits)
