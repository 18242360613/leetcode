class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:return 0
        i,j,nextv=0,-1,[0]*len(needle)
        nextv[0] = -1
        while(i<len(needle)-1):
            if j==-1 or needle[i]==needle[j]:
                i+=1
                j+=1
                nextv[i]=j
            else:
                j=nextv[j]

        i,j=0,0
        while(i<len(haystack) and j<len(needle)):

            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j=nextv[j]

        if j==len(needle):
            return i-j
        else:
            return -1

s = Solution()
print(s.strStr(haystack = "", needle = ""))
