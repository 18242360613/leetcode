class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps,maxd,thres = 0,0,0
        for i in range(len(nums)-1):
            maxd = max(maxd,nums[i]+i)
            if i==thres:
                jumps+=1
                thres=maxd

        return jumps


S = Solution()
ans = S.jump([2,3,1,1,4])
print(ans)