'''Subtree with Maximum Average
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
return the node 11.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    maxAverage, node = 0, None

    def helper(self, root):
        if not root:
            return 0, 0

        leftSum, leftNodes = self.helper(root.left)
        rightSum, rightNodes = self.helper(root.right)

        rootSum = leftSum + rightSum + root.val
        rootNodes = leftNodes + rightNodes + 1

        if not self.node or rootSum * 1.0 > self.maxAverage * rootNodes:
            self.node = root
            self.maxAverage = rootSum * 1.0 / rootNodes
        return rootSum, rootNodes

    def findSubtree2(self, root):
        self.helper(root)
        return self.node
