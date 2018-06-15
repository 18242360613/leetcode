class Solution:

    def dfs(self,ans,cur,n,tem,nums):
        if cur==n:
            ans.append(tem.copy())
            return
        for i in range(n):
            if i==0 or nums[i]!=nums[i-1]:
                c1,c2 = 0,0
                for j in range(n):
                    if nums[j] == nums[i]: c1+=1

                for j in range(cur):
                    if tem[j] == nums[i]: c2+=1

                if c1>c2:
                    tem[cur] = nums[i]
                    self.dfs(ans,cur+1,n,tem,nums)


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans,tem = [],[0]*len(nums)
        self.dfs(ans,0,len(nums),tem,nums)
        return ans

S = Solution()
ans = S.permuteUnique([1,1,1])
print(ans)
