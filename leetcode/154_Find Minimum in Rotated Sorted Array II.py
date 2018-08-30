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

            if nums[mid] == nums[high] and nums[mid] == nums[low]:
                low = low+1
                high = high -1
            else:
                if nums[mid] >= nums[low]:
                    low = mid+1
                else:
                    high = mid
        return nums[low]

s = Solution()
ans = s.findMin([10,1,10,10,10])
print(ans)
