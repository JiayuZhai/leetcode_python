class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        :ref:https://blog.csdn.net/fuxuemingzhu/article/details/80916203
        """
        if len(A) != len(B):
            return False
        diff = 0
        idxs = []
        for i, a in enumerate(A):
            if B[i] != a:
                diff += 1
                idxs.append(i)
        counter = dict()
        if diff == 0:
            for a in A:
                if a in counter and counter[a]:
                    return True
                else:
                    counter[a] = True
        if diff != 2:
            return False
        return A[idxs[0]] == B[idxs[1]] and A[idxs[1]] == B[idxs[0]]
