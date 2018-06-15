class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        K=2
        length = len(prices)
        if length<2:
            return 0
        profit = [[0]*(length) for i in range(K+1)]
        for k in range(1,K+1):
            for i in list(range(1,length)):
                for j in range(i):
                    profit[k][i] = max(profit[k][i-1],profit[k-1][j]+prices[i]-prices[j])
        return profit

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        K=2
        length = len(prices)
        if length<2:
            return 0
        hold1,hold2=-10000000000000,-10000000000000
        release1,release2 = 0,0
        for p in prices:
            hold1 = max(hold1, -p)
            release1 = max(release1, hold1+p)
            hold2 = max(hold2, release1-p)
            release2 = max(release2,hold2+p)
        return release2
        
s = Solution()
print(s.maxProfit([6,1,3,2,4,7]))