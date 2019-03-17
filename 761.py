class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        mem = {}
            
        def solve(s):
            if s not in mem:
                if s.endswith('0'*(len(s)//2)):
                    mem[s] = s
                else:
                    units = []
                    ones = 0
                    b = None
                    for i,c in enumerate(s):
                        if c=='1':
                            if ones == 0:
                                b = i
                            ones += 1
                        else:
                            ones -= 1
                            if ones==0:
                                units.append("1"+solve(s[b+1:i])+"0")
                    mem[s] = "".join(list(sorted(units,reverse=True)))
            return mem[s]
        
        return solve(S)
