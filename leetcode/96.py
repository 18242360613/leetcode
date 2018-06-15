class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in list(range(2, n)):
            for k in range(i):
                dp[i] = dp[i] + dp[k] * dp[i - k - 1]
        return dp[n]

S = Solution()
result = S.numTrees(3)
print(result)