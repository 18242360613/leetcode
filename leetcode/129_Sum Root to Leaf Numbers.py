# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root):
        if root==None:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        res = []
        for numstr in left:
            res.append(str(root.val)+numstr)
        for numstr in right:
            res.append(str(root.val)+numstr)
        if len(left)==0 and len(right)==0 :
            res.append(str(root.val))
        return res

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = self.dfs(root)
        result = 0
        for num in ans:
            result += int(num)
        return result

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

s = Solution()
ans = s.sumNumbers(root)
print(ans)