# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root,sum,ans,tmp):
        if root == None: return

        tmp.append(root.val)

        if root.left == None and root.right == None and root.val==sum:
            ans.append(tmp.copy())

        self.dfs(root.left,sum-root.val,ans,tmp)
        self.dfs(root.right, sum - root.val, ans, tmp)
        tmp.pop()


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(root,sum,ans,[])
        return ans

s = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

ans = s.pathSum(root,22)
print(ans)