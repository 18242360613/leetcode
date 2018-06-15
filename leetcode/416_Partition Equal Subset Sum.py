class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        sums = sum(nums)
        if (sums // 2) * 2 != sums:
            return False
        dp = [0] * ((sums // 2) + 1)
        for i in list(range(1, n)):
            for j in list(range((sums // 2),nums[i]-1,-1)):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return dp[sums // 2] == (sums // 2)

# class Solution():
#     def helper(self,start,nums,target):
#         if target < 0: return
#         elif target == 0: return True
#         for i in range(start,len(nums)):
#             if self.helper(i+1,nums,target-nums[i]):
#                 return True
#         return False
#
#     def canPartition(self, nums):
#         nums.sort(reverse=True)
#         sums = sum(nums)
#         if (sums // 2) * 2 != sums:
#             return False
#         return self.helper(0,nums,(sums // 2))

# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         possible_sums = {0}
#         for n in nums:
#             possible_sums.update({(v + n) for v in possible_sums})
#         return (sum(nums) / 2.)  in possible_sums

s = Solution()
# result = s.canPartition([89,49,21,31,74,56,34,23,35,15,74,59,75,47,16,81,1,32,42,75,4,3,54,55,95,65,10,90,15,23,19,30,24,91,3,84,11,76,6,96,78,84,58,80,28,96,11,46,36,84,3,14,32,86,67,8,60,70,65,57,63,15,61,79,66,55,92,44,62,76,19,52,59,72,2,60,75,52,37,100,1,92,1,40,11,68,61,22,88,70,50,82,81,39,80,75,67,31,3,55])
# result = s.canPartition([91,29,92,14,53,27,96,97,58,76,56,51,68,18,37,98,30,37,25,65,95,22,34,25,29,37,54,34,43,18,65,31,21,91,9,57,13,72,31,26,36,77,85,70,5,72,93,39,46,50,22,16,6,67,17,41,42,10,56,66,69,53,79,46,14,34,80,31,86,78,35,64,75,88,58,26,56,91,84,38,44,19,49,8,4,78,11,13,10,56,72,97,25,62,97,80,20,63,5,27])
result = s.canPartition([48,23,81,49,89,4,29,58,61,91,26,79,81,48,64,1,81,2,36,82,16,97,23,56,50,48,74,50,74,81,10,5,76,66,77,16,19,57,88,89,98,31,16,99,58,84,63,100,79,66,15,62,68,54,29,74,53,83,5,34,42,28,84,62,64,90,29,56,14,69,9,2,45,1,53,5,51,9,42,97,33,42,55,25,96,7,86,79,1,42,94,43,2,16,51,21,40,19,12])
# result = s.canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100])
print(result)