class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split()
        return " ".join(s[::-1])

s = Solution()
ans = s.reverseWords("   a   b ")
print(ans)