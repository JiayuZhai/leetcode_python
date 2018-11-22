class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head ==None:
            return 
        if m ==n:
            return head        
        stack = []
        first = ListNode(0)
        while head:
            stack.append(head.val)
            head = head.next
        stack[m-1:n] = reversed(stack[m-1:n])
        res = first
        while stack:
            first.next = ListNode(stack.pop(0))
            first = first.next
        return res.next
