class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1,x2 = 0,0
        for num in nums:
            x2 = x2^(x1&num)
            x1 = x1^num
            mask = ~(x1&x2)
            x2 = x2&mask
            x1 = x1&mask
        return x1

s = Solution()
ans = s.singleNumber([-2,-2,-4,-2])
print(ans)
