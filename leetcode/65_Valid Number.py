class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        seenE,seenP,seenF,seenN = False,False,False,False
        for i in range(len(s)):
            c = s[i]
            if c == '.':
                if seenE or seenP:return False
                seenP = True
            elif c =='e' :
                if seenE or not seenN:return False
                seenE,seenN = True,False
            elif c == '+' or c == '-':
                if i!=0 and s[i-1]!='e': return False
                seenF,seenN = True,False
            else:
                if not c.isdigit(): return False
                seenN = True
        return seenN

s = Solution()
ans = s.isNumber("e9")
print(ans)
