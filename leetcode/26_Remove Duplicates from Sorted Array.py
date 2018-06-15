class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:return len(nums)
        low,high = 0,1
        while high<len(nums):
            if nums[high]!=nums[low]:
                nums[low+1] = nums[high]
                low+=1
            high+=1
        del nums[low+1:]
        return low+1

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))