class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        e,old = 0.00000001,x
        if x==0:return 0
        while True:
            new = old/2+x/(2*old)
            if abs(new-old)<e:
                break
            old = new
        return int(new)

s = Solution()
ans = s.mySqrt(8)
print(ans)
