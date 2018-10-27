"""234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            pre, slow.next,  slow = slow, pre, slow.next
        if fast:
            slow = slow.next
        while pre and slow:
            if pre.val != slow.val:
                return False
            pre, slow = pre.next, slow.next
        return True
