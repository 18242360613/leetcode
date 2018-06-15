import math
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0: return 0
        column = len(matrix[0])
        dp = [ [0]*column for i in range(row)]
        maxsq = 0

        for i in range(row):
            for j in range(column):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    maxsq = 1

        for i in list(range(1,row)):
            for j in list(range(1,column)):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                    maxsq = max(maxsq,dp[i][j])
                else:
                    dp[i][j] = 0
        return maxsq*maxsq

S = Solution()
result = S.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(result)