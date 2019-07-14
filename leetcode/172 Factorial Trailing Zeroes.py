class Solution:
    def trailingZeroes(self, n):
        count = 0
        while n>0:
            count = count+n//5
            n = n//5
        return count

s = Solution()
ans = s.trailingZeroes(120)
print(ans)