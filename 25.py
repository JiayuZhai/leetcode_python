# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        st = []
        st1=[]
        while(head):
            st.append(head.val)
            head = head.next
        if(len(st)>0):
            gr=int(len(st)/k)
            for i in range(gr):
                for s in range(k):
                    st1.append(st[(i+1)*k-s-1])
            for j in range(len(st)-gr*k):
                st1.append(st[gr*k+j])
            start = ListNode(st1[0])
            result = start
            for m in range(len(st1)-1):
                start.next = ListNode(st1[m+1])
                start = start.next
            return result
        else:
            return None
