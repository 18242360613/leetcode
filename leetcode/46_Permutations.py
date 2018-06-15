class Solution:

    def dfs(self,ans,n,tem,nums):
        if len(tem)==n:
            ans.append(tem.copy())
            return
        for num in nums:
            if num in tem: continue
            tem.append(num)
            self.dfs(ans,n,tem,nums)
            tem.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans,tem = [],[]
        self.dfs(ans,len(nums),tem,nums)
        return ans


S = Solution()
ans = S.permute([1,2,3])
print(ans)