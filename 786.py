class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        ref:https://blog.csdn.net/u010829672/article/details/79594887
        """
        import bisect
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            # A[i] / A[j] = m --> A[i] / m = A[j]，所以通过每个A[i] / m 在通过二分查找可以找比A[j]小的个数
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            # 然后我们用 N-比A[j]小的个数 就是所有不小于A[j]的个数，然后对所有A[j]求和
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                # 找到这个位置之后，把所有可能最大的那个找出来就是最后答案
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])