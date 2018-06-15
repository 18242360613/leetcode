class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can,last_index = True,len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=last_index:
                last_index = i

        return last_index==0

s = Solution()
ans = s.canJump([3,2,1,0,4])
print(ans)