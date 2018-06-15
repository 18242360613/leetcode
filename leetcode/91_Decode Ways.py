class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =="":return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in list(range(1, len(s)+1)):
            if int(s[i-1])>0:
                dp[i] += dp[i-1]
            if 1<i and 10 <=int(s[i-2:i]) and int(s[i-2:i])<27:
                dp[i] += dp[i-2]
        return dp[len(s)]

# class Solution:
#     # @param s, a string
#     # @return an integer
#     def numDecodings(self, s):
#         #dp[i] = dp[i-1] if s[i] != "0"
#         #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
#         if s == "": return 0
#         dp = [0]*(len(s)+1)
#         dp[0] = 1
#         for i in range(1, len(s)+1):
#             if s[i-1] != "0":
#                 dp[i] += dp[i-1]
#             if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
#                 dp[i] += dp[i-2]
#         return dp[len(s)]

s = Solution()
result = s.numDecodings("10")
print(result)