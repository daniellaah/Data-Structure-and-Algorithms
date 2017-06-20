'''Binary Tree Longest Consecutive Sequence
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child (cannot be the reverse).
Example
For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    maxLength = 0
    def helper(self, root):
        if not root:
            return 0

        leftMaxLength = self.helper(root.left)
        rightMaxLength = self.helper(root.right)
        rootMaxlength = 1

        if root.left and root.left.val == root.val + 1:
            rootMaxlength = max(rootMaxlength, leftMaxLength + 1)
        if root.right and root.right.val == root.val + 1:
            rootMaxlength = max(rootMaxlength, rightMaxLength + 1)

        if rootMaxlength > self.maxLength:
            self.maxLength = rootMaxlength
        return rootMaxlength


    def longestConsecutive(self, root):
        # Write your code here
        self.helper(root)
        return self.maxLength
