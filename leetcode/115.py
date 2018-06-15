class Solution:
    def num_Distinct(self, s, i, t, j):

        if j == len(t):
            return 1
        if i == len(s):
            return 0

        sums = 0
        for k in list(range(i,len(s))):
            if s[k] == t[j]:
                sums += self.num_Distinct(s, k+1, t, j + 1)
            else:
                sums += self.num_Distinct(s, k+1, t, j)
            return sums

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return self.num_Distinct(s, 0, t, 0)

s = Solution()
result = s.numDistinct("rabbbit","rabbit")
print(result)