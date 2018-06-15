class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x =1/x
            n=-n
        ans = 1
        while n>0:
            if n&1:
                ans=ans*x
            x=x*x
            n= n>>1
        return ans

s = Solution()
ans = s.myPow(2,-1)
print(ans)