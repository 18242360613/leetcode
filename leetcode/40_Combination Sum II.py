class Solution:
    def dfs(self,candidates, target,ans,path,s):
        if target < 0: return
        if target == 0:
            ans.append(path.copy())
            return
        for i in list(range(s,len(candidates))):
            if i>s and candidates[i-1]==candidates[i]:
                continue
            if target>=candidates[i]:
                path.append(candidates[i])
                self.dfs(candidates,target-candidates[i],ans,path,i+1)
                path.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        self.dfs(candidates,target,ans,[],0)
        return ans

s = Solution()
ans = s.combinationSum([1,1,1,6],8)
print(ans)