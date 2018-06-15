class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nummap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i,num =0,0
        while i<len(s):
            if i+1<len(s):
                if nummap[s[i]]<nummap[s[i+1]]:
                    num=num+(nummap[s[i+1]]-nummap[s[i]])
                    i=i+2
                else:
                    num += nummap[s[i]]
                    i = i + 1
            else:
                num+=nummap[s[i]]
                i=i+1
        return num
