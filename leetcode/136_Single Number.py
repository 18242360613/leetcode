class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        ans = nums[0]
        for num in nums[1:]:
            ans = ans^num
        return ans

s = Solution()
ans = s.singleNumber([4,1,2,1,2])
print(ans)