import sys

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
        ans = []
        self.dfs(candidates,target,ans,[],0)
        return ans[0]

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    candidates,candit = [],{}
    for i in range(N):
        key = int(sys.stdin.readline().strip())
        candidates.append(key)
        candit[key] = i+1
    S = Solution()
    ans = S.combinationSum(candidates,100)
    print(len(ans))
    for i in range(len(ans)):
        print(candit[ans[i]])