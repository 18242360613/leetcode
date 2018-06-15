# class Solution:
#     def isInter(self, s1, i, s2, j, res, s3, dp):
#
#         if i == len(s1) and j == len(s2):
#             if res == s3:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = 0
#             return dp[i][j] == 1
#
#         if dp[i][j] >= 0:
#             return dp[i][j] == 1
#
#         ans = False
#         if i < len(s1):
#             ans = self.isInter(s1, i + 1, s2, j, res + s1[i:i + 1], s3, dp) or ans
#
#         if j < len(s2):
#             ans = self.isInter(s1, i, s2, j + 1, res + s2[j:j + 1], s3, dp) or ans
#
#         if ans:
#             dp[i][j] = 1
#         else:
#             dp[i][j] = 0
#
#         return ans
#
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         dp = [[-1] * (len(s2) + 1) for i in range(len(s1) + 1)]
#         result = self.isInter(s1, 0, s2, 0, "", s3, dp)
#         return result

# class Solution:
#     def isInter(self, s1, i, s2, j, res, s3):
#         if i == len(s1) and j == len(s2):
#             if  res == s3:
#                 return True
#             return False
#
#         ans = False
#         if i < len(s1):
#             ans = self.isInter(s1, i + 1, s2, j, res + s1[i:i + 1], s3) or ans
#
#         if j < len(s2):
#             ans = self.isInter(s1, i, s2, j + 1, res + s2[j:j + 1], s3) or ans
#
#         return ans
#
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         return self.isInter(s1, 0, s2, 0, "", s3)

class Solution:
    def isInter(self, s1, i, s2, j, k, s3, dp):
        if i==len(s1):
            return s2[j:]== s3[k:]

        if j == len(s2):
            return s1[i:] == s3[k:]

        if dp[i][j] >= 0:
            return dp[i][j]==1

        ans = False
        if s1[i:i+1] == s3[k:k+1] and self.isInter(s1, i + 1, s2, j, k+1, s3, dp) :
            ans = True
        if s2[j:j+1] == s3[k:k+1] and self.isInter(s1, i, s2, j+1, k+1, s3, dp):
            ans = True

        if ans:
            dp[i][j] = 1
        else:
            dp[i][j] = 0

        return ans

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp = [[-1] * (len(s2)) for i in range(len(s1))]
        return self.isInter(s1, 0, s2, 0, 0, s3, dp)

s = Solution()
result = s.isInterleave("aabcc","dbbca","aadbbcbcac")
print(result)