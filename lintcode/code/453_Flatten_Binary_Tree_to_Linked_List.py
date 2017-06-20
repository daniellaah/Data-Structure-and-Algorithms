'''Flatten Binary Tree to Linked List
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.
Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
# 递归解法一
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root

        leftLast = self.flatten(root.left)
        rightLast = self.flatten(root.right)
        if leftLast:
            leftLast.right = root.right
            root.right = root.left
        root.left = None
        return rightLast if rightLast else leftLast

# 递归解法二
class Solution(object):
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    last_node = None
    def flatten(self, root):
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.last_node
            root.left = None
            self.last_node = root
