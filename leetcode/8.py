class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        y = 0
        if len(str)==0 or str[0].isalpha(): return 0
        index,i =0,0
        if str[0]=='-' or str[0]=='+':
            index = 1
            i = 1
        while i < len(str):
            if str[i].isdigit():
                i+=1
            else: break
        if i>index:
            y = int(str[:i])
        if y > ((2**31)-1):
            y = ((2**31)-1)
        elif y <(-1)*2**31 :
            y = (-1)*2**31
        return y

S = Solution()
result = S.myAtoi("  120")
print(result)