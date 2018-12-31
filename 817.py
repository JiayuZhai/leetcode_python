# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        :ref: https://blog.csdn.net/shey666/article/details/80527028
        """
        d = {}
        for g in G:
            d[g] = 1
        ans = 0
        flag = 0
        while head:
            if d.get(head.val):
                flag = 1
                if not head.next:
                    ans +=1
            else:
                if flag == 1:
                    ans +=1
                    flag = 0
            head = head.next
        return ans
                
