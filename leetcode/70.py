# class Solution:
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n==1:
#             return 1
#         if n==2:
#             return 2
#         step = [0]*(n+1)
#         step[1] = 1
#         step[2] = 2
        
#         for i in list(range(3,n+1)):
#             step[i] = step[i-1]+step[i-2]
            
#         return step[n]

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        a=1
        b=2
        
        for i in list(range(3,n+1)):
            b,a = a+b,b
            print (a,b)
        return b

s = Solution()
s.climbStairs(5)