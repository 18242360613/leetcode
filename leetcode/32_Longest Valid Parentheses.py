# class Solution:
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         length = len(s)
#         if length < 2: return 0
#         dp = [0] * (length + 1)
#         for i in range(1, length):
#             if s[i] == ")":
#                 if s[i - 1] == "(":
#                     dp[i] = dp[i - 2] + 2
#                 elif s[i - 1] == ")" :
#                     if (i - dp[i-1] - 1>=0) and s[i - dp[i-1] - 1] == '(':
#                         dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
#         return max(dp)

class Solution:
    def longestValidParentheses(self, s):
        stack = []
        length = len(s)
        if length < 2: return 0
        stack.append(-1)
        ans = 0
        for i in range(length):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                ans = max(i - stack[-1],ans)
        return ans


s = Solution()
result = s.longestValidParentheses("(()))())(")
print(result)