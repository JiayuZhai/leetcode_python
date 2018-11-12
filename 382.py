# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.pos = head
        tmp = head
        i=1
        while tmp.next:
            tmp = tmp.next
            i+=1
        self.len = i
        self.start = random.randint(1,self.len)

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = random.randint(1,self.len)
        tmp = self.pos
        while i>0:
            if tmp.next:
                tmp = tmp.next
            else:
                tmp = self.head
            i -=1
        self.pos = tmp
        return tmp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
