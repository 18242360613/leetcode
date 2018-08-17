class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp =[0]*(amount+1)
        dp[0] = 1
        for i in list(range(1,len(coins)+1)):
            for j in list(range(1,amount+1)):
                if j >= coins[i-1]:
                    dp[j] = dp[j] + dp[j-coins[i-1]]

        return dp[amount]

s = Solution()
ans = s.change(3,[1,2])
print(ans)