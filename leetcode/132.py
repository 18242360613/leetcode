class Solution:
    def __init__(self):
        self.word2num={}

    def min_Cut(self, s):
        if s == s[::-1]:
            self.word2num[s] = 0
            return 0

        if s in self.word2num:
            return self.word2num[s]

        mins = len(s) - 1
        for i in range(len(s) - 1):
            left = self.min_Cut(s[:i + 1])
            right = self.min_Cut(s[i + 1:])
            mins = min(left + right + 1, mins)

        self.word2num[s] = mins
        return mins

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.min_Cut(s)

s = Solution()
result = s.min_Cut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
print(result)