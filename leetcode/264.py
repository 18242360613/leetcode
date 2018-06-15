class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2,i3,i5 = 0,0,0
        ugly = [1]
        for i in range(n):
            u2,u3,u5 = ugly[i2]*2,ugly[i3]*3,ugly[i5]*5
            v = min(u2,u3,u5)
            if v == u2:
                i2 += 1
            if v == u3:
                i3 += 1
            if v==u5:
                i5 += 1
            ugly.append(v)
        return ugly[n-1]

s = Solution()
result = s.nthUglyNumber(10)
print(result)