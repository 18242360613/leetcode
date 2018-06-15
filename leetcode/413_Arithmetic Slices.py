# class Solution:
#     def numberOfArithmeticSlices(self, A):
#
#         length = len(A)
#         if length < 3: return 0
#         dp = [0] * (length + 1)
#         ans = 0
#         i = 0
#         while i < length - 2:
#             d = A[i + 1] - A[i]
#             j = i + 2
#             maxlen = 2
#             curlen = 2
#             while j < length:
#                 if (A[j] - A[j - 1])==d:
#                     curlen = j - i + 1
#                     if curlen > maxlen:
#                         dp[j - i + 1] = dp[j - i] * 2 - dp[j - i - 1] + 1
#                         maxlen = j - i + 1
#                 else:
#                     break
#                 j += 1
#             ans += dp[curlen]
#             i = j-1
#         return ans

class Solution:
    def numberOfArithmeticSlices(self, A):
        length = len(A)
        if length <3: return 0
        cont,ans,i = 0,0,2
        while i < length:
            if (A[i]-A[i-1])==(A[i-1]-A[i-2]):
                cont+=1
            else:
                ans=ans+(cont+1)*cont//2
                cont=0
            i += 1
        return ans+(cont+1)*cont//2

s = Solution()
result = s.numberOfArithmeticSlices([1,2,3,4,5,4,3,2,1])
print(result)