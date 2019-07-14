class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n > 0:
            qu,re = divmod(n,26)
            if re == 0:
                qu=qu-1
                ans = 'Z'+ans
            else:
                ans = chr(64+re)+ans
            n = qu
        return ans


S = Solution()
ans = S.convertToTitle(52)
print(ans)