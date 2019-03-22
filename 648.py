class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        tmp=['']*101   #tmp[L]里面是长度为L的所有词根
        for x in dict:
            tmp[len(x)]+=','+x       
        res=sentence.split(' ')
        for i,w in enumerate(res):
            for L in range(1,min(100,len(w))):        #单词的前L位能匹配到词根        
                if w[:L] in tmp[L]:                    
                    res[i]=w[:L]
                    break
        return ' '.join(res)
