# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# division
class Solution:
    def maxmidsum(self,low,mid,high,pricewave):
        leftsum = 0
        rightsum = 0
        sum = 0 
        for i in list(range(mid,low-1,-1)):
            sum+=pricewave[i]
            if sum > leftsum:
                leftsum = sum
        sum = 0
        for j in list(range(mid+1,high+1)):
            sum+=pricewave[j]
            if sum > rightsum:
                rightsum = sum
        return leftsum+rightsum
    
    def findmaxsum(self,low,high,pricewave):
        mid = (low+high)//2
        if low > high:
        	return 0
        elif low == high:
            return pricewave[low]
        else:
            leftsum = self.findmaxsum(low,mid,pricewave)
            rightsum = self.findmaxsum(mid+1,high,pricewave)
            midsum = self.maxmidsum(low,mid,high,pricewave)
        return max(max(leftsum,rightsum),midsum)
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = 0
        pricewave = [a-b for a,b in zip(prices[1:]+[0],prices)][:-1]
        high = len(pricewave)-1
        return max(self.findmaxsum(low,high,pricewave),0)

# dp
# class Solution:        
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         currentsum,maxsum = 0,0
#         for i in list(range(1,len(prices))):
#             currentsum = max(0,currentsum+prices[i]-prices[i-1])
#             maxsum = max(maxsum,currentsum)
#         return maxsum

# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         n = len(prices)
#         if n <= 1:
#             return 0
#         profit = 0
#         currMin = prices[0]
        
#         for p in prices:
#             if p> currMin:
#                 profit = max(p - currMin, profit)
#             else:
#                 currMin = p
        
#         return profit


class Solution:        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        minprice = prices[0]
        maxprofit = 0
        for p in prices:
            if p < minprice:
                minprice=p
            else:
                maxprofit = max(maxprofit,p-minprice)
        return maxprofit

S=Solution()
print(S.maxProfit([10,11,7,10,6]))
# print(S.maxProfit([]))