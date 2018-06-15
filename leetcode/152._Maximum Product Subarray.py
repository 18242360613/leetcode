class Solution:

    def maxProduct(self, nums):
        if len(nums)==0:
            return 0
        res,imax,imin = nums[0],nums[0],nums[0]

        for num in nums[1:]:
            if num<0:
                imax,imin = imin,imax

            imax = max(num,imax*num)
            imin = min(num,imin*num)
            res = max(res,imax)
        return res


s = Solution()
result = s.maxProduct([2,3,-2,-4])
print(result)