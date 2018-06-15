class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        cursum = nums[0]
        maxsum = nums[0]
        for i in list(range(1, length)):
            cursum = nums[i] + max(0, cursum)
            maxsum = max(maxsum, cursum)
        return maxsum

S = Solution()
ans= S.maxSubArray([-1,-2,-3])
print(ans)