class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high = 0,len(nums)-1
        while low < high:
            if nums[low] < nums[high]:
                return nums[low]

            mid = (low+high)//2
            if nums[mid] >= nums[low]:
                low = mid+1
            else:
                high = mid
        return nums[low]

s = Solution()
ans = s.findMin([2,1])
print(ans)
