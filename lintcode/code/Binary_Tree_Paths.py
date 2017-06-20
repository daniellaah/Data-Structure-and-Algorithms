'''Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.
Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
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
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        rootPath = []
        if not root:
            return rootPath
        if not root.left and not root.right:
            rootPath.append(str(root.val))
            return rootPath
        leftPath = self.binaryTreePaths(root.left)
        rightPath = self.binaryTreePaths(root.right)
        for path in (leftPath + rightPath):
            rootPath.append(str(root.val) + '->' + path)
        return rootPath
