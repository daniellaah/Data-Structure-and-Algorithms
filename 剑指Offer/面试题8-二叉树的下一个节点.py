'''面试题8：二叉树的下一个结点
题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。
'''
# 牛客网: https://www.nowcoder.com/questionTerminal/9023a0c988684a53960365b889ceaf5e?source=relative
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # 该点为空, 返回None
        if not pNode:
            return None
        pNext = None
        # 该点的右子树存在, 则返回右子树'最左'的节点
        if pNode.right:
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left
            pNext = pRight
        # 1.该点的右子树不存在,
        # 2.若该点为其父节点的左节点, 则返回这个父节点
        # 3.若该点为其父节点的右节点, 则向上遍历父节点, 重复2
        elif pNode.next:
            pParent = pNode.next
            while pParent and pParent.right is pNode:
                pNode = pParent
                pParent = pParent.next
            pNext = pParent
        return pNext
