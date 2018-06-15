class Solution:
    def countSubstrings(self, s):
        length = len(s)
        nums=0
        subs = [[False]*length for i in range(length)]
        for i in range(length):
            subs[i][i]=True
            tmp = 0
            for j in range(i):
                if (s[i] == s[j]) and (subs[j+1][i-1] or j==i-1):
                    tmp+=1
                subs[j][i] = (s[i] == s[j]) and (subs[j+1][i-1] or j==i-1 )
            nums = nums+tmp+1
        return nums

s = Solution()
print(s.countSubstrings("aabb"))