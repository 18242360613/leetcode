class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for num in nums:
            x = num^x

        x = x&(-x)

        a,b = 0,0
        for num in nums:
            if (num & x)==0:
                a = a^num
            else:
                b = b^num
        return [a,b]

s = Solution()
ans = s.singleNumber([1,2,1,3,2,5])
print(ans)