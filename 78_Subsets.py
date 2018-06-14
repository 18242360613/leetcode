class Solution:
    def dfs(self,start, nums, ans,tmp):
        ans.append(tmp.copy())
        for i in list(range(start,len(nums))):
            tmp.append(nums[i])
            self.dfs(i+1,nums,ans,tmp)
            tmp.pop()

    def subsets(self, nums):
        ans = []
        self.dfs(0,nums,ans,[])
        return ans

s = Solution()
ans = s.subsets([1,2,3])
print(ans)