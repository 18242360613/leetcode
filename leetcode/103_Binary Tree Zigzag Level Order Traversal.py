# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue
class Solution:
    def zigzagLevelOrder(self, root):
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
            if level%2==0:
                tmp.append(t.val)
            else:
                tmp.insert(0,t.val)
            q.put((t.left, level+1))
            q.put((t.right, level+1))
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
S = Solution()
ans =  S.zigzagLevelOrder(root)
print(ans)