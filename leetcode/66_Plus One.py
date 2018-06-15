class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        over,i = 1,len(digits)-1
        while i>=0 and over>0:
            tmp = digits[i]+over
            digits[i],over = tmp%10,tmp//10
            i-=1
        if over:
            digits.insert(0,over)
        return digits

s = Solution()
ans = s.plusOne([9,9,9,9])
print(ans)