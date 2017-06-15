"""109. Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursive(self, start, end):
        if start == end:
            return None
        slow = fast = start
        while fast != end and fast.next != end:
            slow, fast = slow.next, fast.next.next
        root = TreeNode(slow.val)
        root.left = self.recursive(start, slow)
        root.right = self.recursive(slow.next, end)
        return root


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        return self.recursive(head, None)
