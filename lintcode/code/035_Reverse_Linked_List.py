'''35 Reverse Linked List
Reverse a linked list.
Example
For linked list 1->2->3, the reversed linked list is 3->2->1
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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head
        preNode, curNode = None, head
        while curNode:
            nextNode = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = nextNode
        return preNode
