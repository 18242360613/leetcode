class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        strs = [ [] for i in range(numRows)]
        i,lens = 0,len(s)
        while i<lens:
            idx = 0
            while idx < numRows and i<lens:
                strs[idx].append(s[i])
                i+=1
                idx+=1

            idx = numRows-2
            while idx >0 and i<lens:
                strs[idx].append(s[i])
                i+=1
                idx-=1
        res = ""
        for s in strs:
            for c in s:
                res+=c

        return res

s = Solution()
result = s.convert("PAYPALISHIRING",3)
print(result)