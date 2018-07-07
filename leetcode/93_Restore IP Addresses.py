class Solution:
    def vaildString(self,s):
        if len(s)==0 or (len(s)>1 and s[0]=='0') or int(s) > 255:
            return False
        return True

    def dfs(self,cur,ans,s,tmp):
        if len(tmp)==4:
            ans.append('.'.join(tmp.copy()))
            return

        if len(tmp)<3:
            for i in list(range(cur,len(s))):
                tmpstr = s[cur:i]
                if self.vaildString(tmpstr):
                    tmp.append(tmpstr)
                    self.dfs(i,ans,s,tmp)
                    tmp.pop()
        else:
            tmpstr = s[cur:]
            if self.vaildString(tmpstr):
                tmp.append(tmpstr)
                self.dfs(len(s), ans, s, tmp)
                tmp.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(0,ans,s,[])
        return ans

s = Solution()
ans = s.restoreIpAddresses("010010")
print(ans)