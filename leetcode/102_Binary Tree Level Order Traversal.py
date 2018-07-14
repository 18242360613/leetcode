# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        q = queue.Queue()
        q.put((root,0))
        while not q.empty():
            node = q.get()
            t,level= node[0],node[1]
            if t==None:continue
            if len(ans)==level:
                ans.append([])
            tmp = ans[level]
            tmp.append(t.val)
            q.put((t.left, level+1))
            q.put((t.right, level + 1))
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
S = Solution()
ans =  S.levelOrder(root)
print(ans)