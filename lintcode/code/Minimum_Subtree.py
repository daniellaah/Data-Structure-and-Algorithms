'''Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5
return the node 1.
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
    # @return {TreeNode} the root of the minimum subtree
    minSum, node = 0, None
    def helper(self, root):
        if not root:
            return 0
        leftSum = self.helper(root.left)
        rightSum = self.helper(root.right)
        rootSum = leftSum + rightSum + root.val
        if not self.node or rootSum < self.minSum:
            self.node = root
            self.minSum = rootSum
        return rootSum
    def findSubtree(self, root):
        # Write your code here
        self.helper(root)
        return self.node
