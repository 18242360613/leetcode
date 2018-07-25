# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# class Solution:
#     # @param root, a tree link node
#     # @return nothing
#     def connect(self, root):
#         if not root:return
#         p = root.next
#         while p:
#             if p.left:
#                 p = p.left
#                 break
#             if p.right:
#                 p = p.right
#                 break
#             p = p.next
#
#         if root.left:
#             if root.right:
#                 root.left.next = root.right
#             else:
#                 root.left.next = p
#
#         if root.right:
#             root.right.next = p
#
#         self.connect(root.right)
#         self.connect(root.left)

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = TreeLinkNode(0)
        t = dummy
        while root:
            if root.left:
                t.next = root.left
                t = t.next
            if root.right:
                t.next = root.right
                t = t.next
            root = root.next
            if not root:
                t = dummy
                root = dummy.next
                dummy.next = None