'''Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# 解法一递归检查
# from sys import maxsize
# MAX_VALUE = maxsize
# MIN_VALUE = -maxsize - 1
# class Solution:
#     """
#     @param root: The root of binary tree.
#     @return: True if the binary tree is BST, or false
#     """
#     def checkBST(self, root, minValue, maxValue):
#         if not root:
#             return True
#         return minValue < root.val < maxValue and \
#                 self.checkBST(root.left, minValue, root.val) and \
#                 self.checkBST(root.right, root.val, maxValue)
#     def isValidBST(self, root):
#         # write your code here
#         return self.checkBST(root, MIN_VALUE, MAX_VALUE)

# 解法二中序遍历
from sys import maxsize
MIN_VALUE = -maxsize - 1
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    lastValue = MIN_VALUE
    def isValidBST(self, root):
        # write your code here
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.lastValue:
            return False
        self.lastValue = root.val
        return self.isValidBST(root.right)
