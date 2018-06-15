class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [a for a in triangle[-1]]
        for layer in list(range(len(triangle)-2, -1,-1)):
            for i in range(len(triangle[layer])):
                dp[i] = min(dp[i],dp[i+1])+triangle[layer][i]

        return dp[0]

s = Solution()
result = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(result)