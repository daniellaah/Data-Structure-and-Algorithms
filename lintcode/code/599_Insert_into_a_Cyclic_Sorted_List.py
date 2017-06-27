'''599 Insert into a Cyclic Sorted List
Given a node from a cyclic linked list which has been sorted, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be any single node in the list. Return the inserted new node.

 Notice

3->5->1 is a cyclic list, so 3 is next node of 1.
3->5->1 is same with 5->1->3

Example
Given a list, and insert a value 4:
3->5->1
Return 5->1->3->4
'''


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param {ListNode} node a list node in the list
    # @param {int} x an integer
    # @return {ListNode} the inserted new list node
    def insert(self, node, x):
        # Write your code here
        if not node:
            node = ListNode(x)
            node.next = node
            return node
        pre, p = node, node.next
        while p != node:
            if pre.val <= x <= p.val:
                break
            if pre.val > p.val and (x > pre.val or x < p.val):
                break
            pre = p
            p = p.next
        newNode = ListNode(x)
        newNode.next = p
        pre.next = newNode
        return newNode
