class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/80644702
        """
        _len = len(S)
        shifts_sum = sum(shifts)
        shifts_real = []
        for shift in shifts:
            shifts_real.append(shifts_sum)
            shifts_sum -= shift
        def shift_map(string, shift_time):
            shifted = ord(s) + (shift_time % 26)
            return chr(shifted if shifted <= ord('z') else shifted - 26)
        ans = ''
        for i, s in enumerate(S):
            ans += shift_map(s, shifts_real[i])
        return ans
