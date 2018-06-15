import sys

sys.setrecursionlimit(1100)


# class Solution:
#     def minSteps(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # global minstep
#
#         def findstep(n, cur, step, cont):
#             if cur == n:
#                 return step
#             elif cur < n and step<=n:
#                 a = findstep(n, cur, step + 1, cur)  # copy
#                 b = findstep(n, cur + cont, step + 1, cont)  # paste
#                 return min(a, b)
#             else:
#                 return 100000
#
#         return findstep(n, 1, 0, 1)+1

class Solution(object):
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans

S = Solution()
print(S.minSteps(31))