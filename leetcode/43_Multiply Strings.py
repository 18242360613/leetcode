class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1,len2 = len(num1),len(num2)
        pos = [0]*(len1+len2)
        for i in list(range(len1 - 1, -1, -1)):
            for j in list(range(len2 - 1, -1, -1)):
                num = int(num1[i])*int(num2[j])
                p1,p2 = i+j,i+j+1
                sums = num+pos[p2]
                pos[p1] += sums//10
                pos[p2] = sums%10
        ans = ""
        for num in pos:
            if not (num==0 and len(ans)==0):
                ans+=str(num)

        if len(ans)>0:return ans
        return "0"

S = Solution()
ans = S.multiply("123","456")
print(ans)