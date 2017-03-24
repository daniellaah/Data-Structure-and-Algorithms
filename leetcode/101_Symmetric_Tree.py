"""101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution(object):
    def isSameVal(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.isSameVal(left.left, right.right) and self.isSameVal(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSameVal(root.left, root.right)

# 非递归
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_stack, right_stack = [], []
        left_stack.append(root.left)
        right_stack.append(root.right)
        while left_stack and right_stack:
            left = left_stack.pop()
            right = right_stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            left_stack.append(left.left)
            left_stack.append(left.right)
            right_stack.append(right.right)
            right_stack.append(right.left)
        return True
