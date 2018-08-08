class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        path,sum = [-1]*(amount+1),[float('inf')]*(amount+1)
        path[0],sum[0] = -1,0
        for s in list(range(1,amount+1)):
            for c in coins:
                if s >=c and sum[s] > sum[s-c]+1:
                    sum[s] = sum[s-c]+1
                    path[s] = c

        if sum[amount]!=float("inf"):
            return sum[amount]
        else:
            return -1


s = Solution()
ans = s.coinChange([1,2,5],11)
print(ans)