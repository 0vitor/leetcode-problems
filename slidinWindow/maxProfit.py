class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i,j = 0, 0
        
        maxP = 0
        while j < len(prices) and i < len(prices):
            if prices[i] <= prices[j]:
                maxP = max(maxP, prices[j] - prices[i])
                j += 1
            elif prices[i] > prices[j]:
                i = j

        return maxP

Solution().maxProfit([3,3])        
