"""114. Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法一, 前序遍历, 使用额外空间
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        preorder, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                preorder.append(node)
                stack.append(node.right)
                stack.append(node.left)
        for i in range(len(preorder) - 1):
            preorder[i].right = preorder[i+1]
            preorder[i].left = None
# 解法二, 递归. 简化版见解法三
class Solution(object):
    def recursive(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        if not root.left and root.right:
            return self.recursive(root.right)
        if not root.right and root.left:
            root.right = root.left
            root.left = None
            return self.recursive(root.right)
        left_last = self.recursive(root.left)
        right_last = self.recursive(root.right)
        left_last.right = root.right
        root.right = root.left
        root.left = None
        return right_last

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.recursive(root)
# 解法三, 解法二的简化版
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def recursive(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        left_last = self.recursive(root.left)
        right_last = self.recursive(root.right)
        if left_last:
            left_last.right = root.right
            root.right = root.left
        root.left = None
        return right_last if right_last else left_last

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.recursive(root)
