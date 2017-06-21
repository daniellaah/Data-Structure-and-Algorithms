'''Binary Tree Path Sum
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.
Example
Given a binary tree, and target = 5:

     1
    / \
   2   4
  / \
 2   3
return

[
  [1, 2, 2],
  [1, 4]
]
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        if not root:
            return []
        if not root.right and not root.left and root.val == target:
            return [[root.val]]
        leftPathSum = self.binaryTreePathSum(root.left, target - root.val)
        rightPathSum = self.binaryTreePathSum(root.right, target - root.val)
        rootPathSum = []
        for path in (leftPathSum + rightPathSum):
            rootPathSum.append([root.val] + path)
        return rootPathSum
