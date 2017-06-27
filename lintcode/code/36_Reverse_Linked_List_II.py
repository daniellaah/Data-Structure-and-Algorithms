'''36 Reverse Linked List II
Reverse a linked list from position m to n.

 Notice

Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.
Example
Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
'''
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or not head.next or not m or not n:
            return head
        headNode = ListNode(0)
        headNode.next = head
        for i in range(m-1):
            headNode = headNode.next
        preNode = headNode.next
        curNode = preNode.next
        for i in range(n - m):
            nextNode = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = nextNode
        tailNode = preNode
        headNode.next.next = curNode
        headNode.next = tailNode
        return headNode.next if m == 1 else head
