'''450 Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
Example
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        if not head or not k or k <= 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        headNode = dummy
        while headNode:
            headNode = self.reverseKNodes(headNode, k)
        return dummy.next

    def reverseKNodes(self, headNode, k):
        preNode = headNode
        for i in range(k):
            if not preNode:
                return None
            preNode = preNode.next
        if not preNode:
            return None
        preNode = headNode.next
        curNode = preNode.next
        for i in range(k-1):
            nextNode = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = nextNode
        headNode.next.next = curNode
        nextHeadNode = headNode.next
        headNode.next = preNode
        return nextHeadNode
