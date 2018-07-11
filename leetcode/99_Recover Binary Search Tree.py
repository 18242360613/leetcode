# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = TreeNode(-float("inf"))

    def in_order(self, root):
        if not root:
            return

        self.in_order(root.left)

        if self.first==None and self.pre.val > root.val:
            self.first = self.pre

        if self.first != None and self.pre.val >root.val:
            self.second = root
        self.pre = root

        self.in_order(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.in_order(root)
        self.first.val,self.second.val = self.second.val,self.first.val
