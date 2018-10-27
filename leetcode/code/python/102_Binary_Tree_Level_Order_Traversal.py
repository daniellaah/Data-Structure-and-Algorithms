"""102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            lr_pairs = [(node.left, node.right) for node in level]
            level = [lr for lr_pair in lr_pairs for lr in lr_pair if lr]
        return ans
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue, ret, level = [], [], []
        right = next_right = root
        queue.append(root)
        while queue:
            current = queue.pop(0)
            level.append(current.val)
            if current.left:
                queue.append(current.left)
                next_right = current.left
            if current.right:
                queue.append(current.right)
                next_right = current.right
            if current is right:
                ret.append(level)
                level = []
                right = next_right
        return ret
