"""Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL."""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        # 找出最后一个节点
        cur = head
        size = 1
        while cur.next:
            cur = cur.next
            size += 1
        last = cur

        # 找出有效的k
        k %= size
        if k == 0:
            return head

        step = size - k - 1
        cur = head
        for i in range(step):
            cur = cur.next
        last.next = head
        head = cur.next
        cur.next = None
        return head
