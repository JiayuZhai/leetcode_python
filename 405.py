class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        s = 0
        if num < 0:
            for i in range(8):
                s += 16 ** i * 15
            num = s + num + 1
        a = []
        while num > 0:
            a.append(num % 16)
            num //= 16
        r = ''
        for i in a[::-1]:
            if i == 10:
                r += 'a'
                continue
            if i == 11:
                r += 'b'
                continue
            if i == 12:
                r += 'c'
                continue
            if i == 13:
                r += 'd'
                continue
            if i == 14:
                r += 'e'
                continue
            if i == 15:
                r += 'f'
                continue
            r += str(i)
        return r
