class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap = [0] * n
        not_swap = [0] * n
        swap[0] = 1
        for i in range(1, n):
            if A[i - 1] >= B[i] or B[i - 1] >= A[i]:
                swap[i] = swap[i - 1] + 1
                not_swap[i] = not_swap[i - 1]
            elif A[i - 1] >= A[i] or B[i - 1] >= B[i]:
                swap[i] = not_swap[i - 1] + 1
                not_swap[i] = swap[i - 1]
            else:
                tmp = min(swap[i - 1], not_swap[i - 1])
                swap[i] = tmp + 1
                not_swap[i] = tmp
        return min(not_swap[-1], swap[-1])
