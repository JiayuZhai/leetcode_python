class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        listN = [int(num) for num in str(n)]
        canChange = False

        for i in range(len(listN) - 2, -1, -1):
            if listN[i] < listN[i+1]:
                for j in range(len(listN)-1, -1, -1):
                    if listN[i] < listN[j]:
                        listN[i], listN[j] = listN[j], listN[i]
                        break
                canChange = True
                break
        if not canChange: return -1
        else:
            newList = listN[:i+1] + sorted(listN[i+1:])
            result = int(''.join(str(num) for num in newList))
            if result > 2**31 - 1: return -1
            else: return result
