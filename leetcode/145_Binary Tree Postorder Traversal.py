# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ans,nodes = [],[root]
        while len(nodes)!=0:
            cur = nodes.pop()
            ans.append(cur.val)
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
        return ans[::-1]
