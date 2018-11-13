# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        :ref:https://blog.csdn.net/liuxiao214/article/details/77803348
        """
        if head==None or head.next==None:
            return True
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        def reverselist(head):
            pre=None
            ne=None
            while head!=None:
                ne=head.next
                head.next=pre
                pre=head
                head=ne
            return pre
        slow.next=reverselist(slow.next)
        slow=slow.next
        while slow!=None:
            if slow.val!=head.val:
                return False
            slow=slow.next
            head=head.next
        return True
