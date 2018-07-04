class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":return True
        ls,lt,i,j = len(s),len(t),0,0
        while i <lt:
            if j==ls:return True
            if t[i]==s[j]:
                j+=1
            i+=1
        return j==ls

s = Solution()
ans = s.isSubsequence(s = "abc", t = "ahbgdc")
print(ans)