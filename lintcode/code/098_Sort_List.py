'''98 Sort List
Sort a linked list in O(n log n) time using constant space complexity.
Example
Given 1->3->2->null, sort it to 1->2->3->null.
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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def findMid(self, head):
        if not head:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        curNode = head
        while l1 and l2:
            if l1.val < l2.val:
                curNode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curNode.next = ListNode(l2.val)
                l2 = l2.next
            curNode = curNode.next
        if l1:
            curNode.next = l1
        if l2:
            curNode.next = l2
        return head.next

    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        rightHead = self.sortList(mid.next)
        mid.next = None
        leftHead = self.sortList(head)
        return self.merge(leftHead, rightHead)
