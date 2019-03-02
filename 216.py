class Solution:
    choices = list(range(1, 10))
    
    def a(self, k, n, choices):
        ret = []
        if k == 1:
            if n in choices:
                return [[n]]
            else:
                return []
        for i, c in enumerate(choices):
            if c < n:
                ret.extend([[c] + sol for sol in self.a(k-1, n-c, choices[i+1:])])
        return ret
            
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        choices = self.choices
        return self.a(k, n, choices)
