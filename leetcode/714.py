# class Solution:
#     def maxProfit(self, prices, fee):
#         """
#         :type prices: List[int]
#         :type fee: int
#         :rtype: int
#         """
#         cash, hold = 0, -prices[0]
#         for i in range(1, len(prices)):
#             cash = max(cash, hold + prices[i] - fee)
#             hold = max(hold, cash - prices[i])
#             print(cash,hold)
#         return cash  

# s=Solution()
# s.maxProfit([1,3,2,8,4,9],2)


class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i])
            hold = max(hold, cash - prices[i] - fee)
        return cash  

class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int s0 = 0, s1 = -50010; 
        for(int p:prices) {
            s0 = max(s0, s1+p);
            s1 = max(s1, s0-p-fee);
        }
        return s0;
    }
};

# class Solution {
# public:
#     int maxProfit(vector<int>& prices, int fee) {
#         int s0 = 0, s1 = -50010; 
#         for(int p:prices) {
#             s0 = max(s0, s1+p-fee);
#             s1 = max(s1, s0-p);
#         }
#         return s0;
#     }
# };