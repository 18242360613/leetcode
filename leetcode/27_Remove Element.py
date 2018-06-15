class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        low,high = 0,0
        while high < len(nums):
            if nums[high]!=val:
                nums[low]=nums[high]
                low+=1
            high+=1
        return low

s = Solution()
print(s.removeElement([2],2))