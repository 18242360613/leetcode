class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,h = 0,len(nums)
        while l<h:
            mid = (l+h)//2
            if nums[mid] == target:return mid
            if nums[mid]>nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    h = mid
                else:
                    l = mid+1
            else:
                if nums[mid] < target and target <= nums[h-1]:
                    l = mid+1
                else:
                    h =mid
        return -1

s = Solution()
result = s.search([3,1],1)
print(result)