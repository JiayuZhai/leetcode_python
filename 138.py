"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #新链表 pre 是新链表的虚拟头节点
        pre = Node(-1,None,None)
        tail = pre
        d = {}

        #第一次遍历，建立新链表
        oldNode = head
        while oldNode:
            newNode = Node(oldNode.val,None,None)
            d[oldNode] = newNode  #把新的节点和原始的节点放入dic
            tail.next = newNode
            tail = tail.next
            oldNode = oldNode.next
        
        #第二次遍历，赋值random指针
        tail = pre.next  #两个指针分别指向链表的头部
        oldNode = head
        while oldNode:
            if oldNode.random:
                tail.random = d[oldNode.random]
            oldNode = oldNode.next
            tail = tail.next

        return pre.next
