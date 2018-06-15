class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[0] * (lp + 1) for i in range(ls + 1)]
        dp[0][0] = 1
        for j in range(1, lp + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] != p[j - 2]:
                        dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]

        return dp[ls][lp]==1

s = Solution()
result = s.isMatch('aaa','ab*a')
print(result)