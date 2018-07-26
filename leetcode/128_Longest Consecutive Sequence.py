class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        maxlen,i,j = 0,0,0
        while i < len(nums):
            j = i
            while j < len(nums) and (j-i)==(nums[j]-nums[i]):
                if j-i+1>maxlen:
                    maxlen = j-i+1
                j+=1
            i = j
        return maxlen

s = Solution()
ans = s.longestConsecutive([100,4,200,1,3,-1,-2,0,2])
print(ans)
