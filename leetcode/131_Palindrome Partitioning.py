# class Solution:
#
#     def dfs(self,ans,start,end,templist,s):
#         if start==end:
#             ans.append(templist.copy())
#             return
#
#         for i in list(range(start,end)):
#             tmp = s[start:i+1]
#             if tmp==tmp[::-1]:
#                 templist.append(tmp)
#                 self.dfs(ans,i+1,end,templist,s)
#                 templist.pop()
#
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         ans = []
#         self.dfs(ans,0,len(s),[],s)
#         return ans

class Solution:
    def dfs(self,s,dp,pos,ans,templist):
        if pos==len(s):
            ans.append(templist.copy())
            return
        for i in list(range(pos,len(s))):
            if dp[pos][i]:
                templist.append(s[pos:i+1])
                self.dfs(s,dp,i+1,ans,templist)
                templist.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp=[[0]*(len(s)) for i in range(len(s))]
        for l in list(range(len(s))):
            for start in list(range(0,len(s)-l)):
                if (s[start]==s[start+l] )and (l<=2 or dp[start+1][start+l-1]):
                    dp[start][start+l] = 1
        ans = []
        self.dfs(s,dp,0,ans,[])
        return ans



s = Solution()
ans = s.partition("abbab")
print(ans)