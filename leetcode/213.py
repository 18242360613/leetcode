import sys

class Solution:

    def sin_rob(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        a = nums[0]
        b = max(nums[0], nums[1])
        for i in list(range(2, length)):
            b, a = max(a + nums[i], b), b
        return max(a, b)

    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        return max(self.sin_rob(nums[1:]), self.sin_rob(nums[:-1]))

S = Solution()
result = S.rob([1,2,3,4,5,6,7,1,8])
print(result)