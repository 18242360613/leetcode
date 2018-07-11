# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root,lessThan = float("inf"),largeThan=-float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif root.val >= lessThan or root.val <= largeThan:
            return False
        return self.isValidBST(root.left,min(lessThan,root.val),largeThan) and self.isValidBST(root.right,lessThan,max(largeThan,root.val))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(20)

s = Solution()
ans = s.isValidBST(root)
print(ans)