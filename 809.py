class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def wlist(string):
            temp = []
            count = 1
            s_l = len(string)
            if (s_l == 0):
                return [['', 0]]

            for i in range(s_l - 1):
                if (string[i] == string[i + 1]):
                    count = count + 1
                else:
                    temp.append([string[i], count])
                    count = 1
            temp.append([string[-1], count])
            return temp

        st = wlist(S)
        st_l = len(st)
        # print(st)

        result = 0

        for j, w in enumerate(words):
            wt = wlist(w)
            if (len(wt) == st_l):
                wcount = 0
                for k in range(st_l):
                    if (st[k][0] == wt[k][0]):
                        if (st[k][1] == wt[k][1]):
                            wcount = wcount + 1
                        elif (st[k][1] > wt[k][1] and st[k][1] >= 3):
                            wcount = wcount + 1
                        else:
                            continue
                if (wcount == st_l):
                    result = result + 1

        return result 
