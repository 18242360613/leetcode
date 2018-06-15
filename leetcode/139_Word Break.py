class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                j = len(word)
                if (i + 1) >= j:
                    if s[i + 1 - j:i+1] == word:
                        dp[i + 1] = dp[i + 1 - j] or dp[i + 1]
        return dp[len(s)]

s = Solution()
result = s.wordBreak("leetcode",["leet","code"])
print(result)