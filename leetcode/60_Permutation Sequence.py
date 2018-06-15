class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums,fac = [i+1 for i in range(n)],[]
        fac.append(1)
        for i in list(range(1,n+1)):
            fac.append(fac[-1]*i)

        k,ans = k-1,""
        for i in list(range(1,n+1)):
            index = k//fac[n-i]
            ans = ans+str(nums[index])
            nums.pop(index)
            k = k - index*fac[n-i]
        return ans

s = Solution()
ans = s.getPermutation(4,24)
print(ans)