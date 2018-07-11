# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif (p==None and q!=None) or (p!=None and q==None):
            return False

        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        cur = (p.val==q.val)
        return left and right and cur

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

s = Solution()
ans = s.isSameTree(p,q)
print(ans)