"""98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from sys import maxsize
# 解法一, 中序遍历, 非递归
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        last_node, stack = -maxsize - 1, []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if node.val <= last_node:
                    return False
                last_node = node.val
                root = node.right
        return True
# 解法二, 中序遍历, 递归
from sys import maxsize
MIN_VALUE = -maxsize - 1
class Solution(object):
    pre_val = MIN_VALUE
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre_val:
            return False
        self.pre_val = root.val
        if not self.isValidBST(root.right):
            return False
        return True
# 解法三, 递归检查
from sys import maxsize
MAX_VALUE = maxsize
MIN_VALUE = -maxsize - 1
class Solution(object):
    def checkBST(self, root, min_value, max_value):
        if not root:    return True
        return min_value < root.val < max_value and \
                self.checkBST(root.left, min_value, root.val) and \
                self.checkBST(root.right, root.val, max_value)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkBST(root, MIN_VALUE, MAX_VALUE)
