'''105 Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
        # 相邻复制
        preNode = head
        while preNode:
            nextNode = preNode.next
            copyNode = RandomListNode(preNode.label)
            preNode.next = copyNode
            copyNode.next = nextNode
            preNode = nextNode
        # 连接random
        node = head
        while node:
            copyNode = node.next
            if node.random:
                copyNode.random = node.random.next
            else:
                copyNode.random = None
            node = copyNode.next
        # 拆回两个链表
        copyHead = head.next
        node = head
        while node:
            copyNode = node.next
            node.next = copyNode.next
            node = copyNode.next
            if node:
                copyNode.next = node.next
            else:
                copyNode.next = None
        return copyHead
