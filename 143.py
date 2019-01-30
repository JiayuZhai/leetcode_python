# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        #快慢指针找到链表中点s
        f = s = head
        while f and f.next:
            s = s.next
            f = f.next.next
        #中点之后的链表反转
        p = c = s
        n = c.next
        while n:
            p = c
            c = n
            n = n.next
            c.next = p
        #c为末尾节点，双指针分别从头结点和末尾节点重构链表
        n1 = h1 = head
        n2 = h2 = c
        while h1 != h2 and h1.next != h2:
            n1 = h1.next
            n2 = h2.next
            h1.next = h2
            h2.next = n1
            h1 = n1
            h2 = n2
        h2.next = None
