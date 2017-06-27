'''165 Merge Two Sorted Lists
Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
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
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        current = head
        while l1 and l2:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next
        if l1:
            while l1:
                current.next = ListNode(l1.val)
                l1 = l1.next
                current = current.next
        if l2:
            while l2:
                current.next = ListNode(l2.val)
                l2 = l2.next
                current = current.next
        return head.next
