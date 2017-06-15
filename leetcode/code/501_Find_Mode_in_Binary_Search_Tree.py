"""501. Find Mode in Binary Search Tree
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = []
    currentVal, currentMode, maxMode = 0, 0, 0

    def inorder(self, root):
        if root:
            self.inorder(root.left)

            self.currentMode += 1
            if self.currentVal != root.val:
                self.currentVal, self.currentMode = root.val, 1
            if self.currentMode > self.maxMode:
                self.maxMode = self.currentMode
                self.result = []
                self.result.append(self.currentVal)
            elif self.currentMode == self.maxMode:
                self.result.append(self.currentVal)

            self.inorder(root.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.inorder(root)
        return self.result
