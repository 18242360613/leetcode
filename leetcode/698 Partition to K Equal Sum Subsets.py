# class Solution:
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         target, rem = divmod(sum(nums), k)
#         if rem: return False
#
#         def dfssearch(target,k,cursum,visited,startindex):
#             if k==1: return True
#             if target==cursum:
#                 return dfssearch(target,k-1,0,visited,0)
#             for i in list(range(startindex,len(nums))):
#                 if visited[i]!=1:# not visited
#                     visited[i] = 1
#                     if dfssearch(target,k,cursum+nums[i],visited,i+1):
#                         return True
#                     visited[i] = 0
#             return False
#         visited = [0]*len(nums)
#         return dfssearch(target,k,0,visited,0)

# class Solution:
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         if sum(nums) % k != 0: return False;
#         SUM = sum(nums) / k;
#
#         nums = sorted(nums, reverse=True)
#         visited = [0] * len(nums)
#         curPos, curGroup, curSum = 0, 0, 0
#
#         def DFS(curPos, curGroup, curSum):
#             if curGroup == k: return True
#             if curSum == SUM: return DFS(0, curGroup + 1, 0)
#             if curPos >= len(nums): return False
#             if curSum > SUM: return False
#             for i in range(curPos, len(nums)):
#                 if visited[i] == 1: continue
#                 if i != curPos and nums[i] == nums[i - 1] and visited[i - 1] == 0: continue;
#                 visited[i] = 1
#                 if DFS(i + 1, curGroup, curSum + nums[i]): return True
#                 visited[i] = 0
#             return False
#
#         return DFS(curPos, curGroup, curSum)

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target: return False

        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in range(1 << len(nums)):
            if not dp[state]: continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if (num <= target - (total[state] % target)):
                        dp[future] = True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]

s = Solution()
result = s.canPartitionKSubsets([5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,3],15)
print(result)