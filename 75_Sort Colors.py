class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,l,h = 0,0,len(nums)-1
        while i<=h:
            if nums[i]==0:
                nums[i],nums[l] = nums[l],nums[i]
                l+=1
            elif nums[i]==2:
                nums[i],nums[h] = nums[h],nums[i]
                h=h-1
                i-=1
            i+=1



s = Solution()
nums=[1,2,0]
s.sortColors(nums)
print(nums)