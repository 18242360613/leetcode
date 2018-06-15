class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,h = 0,len(nums)
        while l<h:
            mid = (l+h)//2
            if nums[mid] < target:
                l=mid+1
            else:
                h=mid
        return l

s = Solution()
result = s.searchInsert([5,7,7,8,8,10],11)
print(result)