# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        while head:
            next = head.next
            p = dummy
            c = dummy.next
            while c and head.val >= c.val:
                c = c.next
                p = p.next
            p.next = head
            head.next = c
            head = next
        return dummy.next
