class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0,1]
        if n==0:return [0]
        for i in list(range(1,n)):
            count = len(ans)
            while count:
                count = count - 1
                ans.append(ans[count]+(1<<i))
        return ans

S = Solution()
ans = S.grayCode(4)
print(ans)