class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,t = 0,len(s)-1
        while t>=0 and s[t]==' ':t-=1
        while t>=0 and s[t]!=' ':
            t-=1
            l+=1
        return l
S = Solution()
ans = S.lengthOfLastWord("Hello World")
print(ans)