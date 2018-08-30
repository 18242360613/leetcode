class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versionnum1 = [int(num) for num in version1.split(".")]
        versionnum2 = [int(num) for num in version2.split(".")]
        length1,length2,i = len(versionnum1),len(versionnum2),0
        while i <length1 and i < length2:
            if versionnum1[i] < versionnum2[i]:
                return -1
            elif versionnum1[i] > versionnum2[i]:
                return 1
            i+=1
        if i < length1:
            if sum(versionnum1[i:])==0:
                return 0
            return 1
        elif i < length2:
            if sum(versionnum2[i:])==0:
                return 0
            return -1
        else:
            return 0

s = Solution()
ans = s.compareVersion("2","2.0")
print(ans)