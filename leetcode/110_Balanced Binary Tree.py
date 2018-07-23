# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root):
        if root == None: return True,0
        bl,left = self.dfs(root.left)
        br,right = self.dfs(root.right)
        if abs(left-right)>1:
            return False,max(left,right)+1
        return bl and br,max(left,right)+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bance,_ = self.dfs(root)
        return bance

s = Solution()
root = TreeNode(1)
ans = s.isBalanced(root)
print(ans)