class Solution:
    # "ZY"->701
    def titleToNumber(self, s) -> int:
        s = s[::-1]
        ans = 0
        for i in range(len(s)):
            ans = (ord(s[i])-64)*(26**i)+ans
        return ans

S = Solution()
print(S.titleToNumber('A'))