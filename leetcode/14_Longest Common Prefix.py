import os
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return  os.path.commonprefix(strs)

s = Solution()
result = s.longestCommonPrefix(["flowerrr","flow","fgwht"])
print(result)