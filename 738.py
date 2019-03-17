class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n = str(N)
        num = list(n)

        nine = len(num)
        for i in range(len(num) - 1, 0, -1):
            if num[i - 1] > num[i]:
                num[i - 1] = str(int(num[i - 1]) - 1)
                nine = i

        num = ''.join(num)
        num = int(num[:nine] + '9' * (len(num) - nine))
        return num
