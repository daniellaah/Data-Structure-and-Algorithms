'''面试题6：从尾到头打印链表
题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
'''
from random import randint
class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

def print_linked_list_inverse(head):
    if not head:
        return
    if not head.next:
        print(head.val, end=', ')
    else:
        print_linked_list_inverse(head.next)
        print(head.val, end=', ')


if __name__ == "__main__":
    nums = [randint(1, 10) for _ in range(10)]
    head = Node(nums[0])
    p = head
    for num in nums[1:]:
        p.next = Node(num)
        p = p.next
    print(nums)
    print_linked_list_inverse(head)
