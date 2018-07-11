# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# import queue
# class Solution:
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         q1,q2 = queue.Queue(),queue.Queue()
#         q1.put(root)
#         q2.put(root)
#         while not q1.empty() and not q2.empty():
#             t1,t2 = q1.get(),q2.get()
#             if t1==None and t2==None:continue
#             if t1==None or t2==None: return False
#             if t1.val != t2.val: return False
#             q1.put(t1.left)
#             q1.put(t1.right)
#             q2.put(t2.right)
#             q2.put(t2.left)
#         if q1.empty() and q2.empty():
#             return True
#         return False

import queue
class Solution:
    def ismirror(self,t1,t2):
        if t1==None and t2==None:return True
        if t1==None or t2==None:return False
        return (t1.val==t2.val) and self.ismirror(t1.left,t2.right) and self.ismirror(t1.right,t2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.ismirror(root,root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
S = Solution()
ans = S.isSymmetric(root)
print(ans)