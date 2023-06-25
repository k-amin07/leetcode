from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in prices:
            currentProfit = i - minPrice
            minPrice = min(minPrice,i)
            maxProfit = max(maxProfit,currentProfit)
        return maxProfit
