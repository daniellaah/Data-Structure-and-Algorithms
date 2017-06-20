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
    _minSum, _node = 0, None
    def helper(self, root):
        if not root:
            return 0
        rootSum = self.helper(root.left) + \
                    self.helper(root.right) + \
                    root.val
        if not self._node or rootSum < self._minSum:
            self._node = root
            self._minSum = rootSum
        return rootSum

    def findSubtree(self, root):
        # Write your code here
        self.helper(root)
        return self._node
