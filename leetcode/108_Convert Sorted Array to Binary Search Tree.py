# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def create_tree(self,low,high,nums):
        if low>high: return None
        mid = (low+high)//2
        root = TreeNode(nums[mid])
        root.left = self.create_tree(low,mid-1,nums)
        root.right = self.create_tree(mid+1,high,nums)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        low,high = 0,len(nums)-1
        return self.create_tree(low,high,nums)

s = Solution()
root = s.sortedArrayToBST([-10,-3,0,5,9])
print("")